/*
 * File: 103-python.c
 * Auth: Brennan D Baraban
 */
#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
/**
 * print_python_list - print basic info about Python lists
 * @p: Python list
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyObject *item;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %zd\n", PyList_Size(p));
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

for (i = 0; i < PyList_Size(p); i++)
{
item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
}
}
/**
 * print_python_bytes - print basic info about Python bytes
 * @p: Python bytes
 */
void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %zd bytes:", (size < 10 ? size : 10));
    for (i = 0; i < size && i < 10; i++) {
        printf(" %02x", (unsigned char)str[i]);
    }
    printf("\n");
}
/**
 * print_python_float - print basic info about Python float
 * @p: Python float number
 */
void print_python_float(PyObject *p)
{
double value;

printf("[.] float object info\n");
if (!PyFloat_Check(p))
{
printf("  [ERROR] Invalid Float Object\n");
return;
}

value = PyFloat_AsDouble(p);
printf("  value: %g\n", value);
}
