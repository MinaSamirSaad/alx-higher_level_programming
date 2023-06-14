#include <Python.h>
/**
 * print_python_list - Prints information about a Python list object
 * @p: Pointer to the PyObject representing the list
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyObject *obj;

size = PyList_Size(p);
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
obj = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to the PyObject representing the bytes object
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *str;

printf("[.] bytes object info\n");

if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = ((PyVarObject *)p)->ob_size;
str = ((PyBytesObject *)p)->ob_sval;

printf("  size: %ld\n", size);
printf("  trying string: %s\n", str);

printf("  first %ld bytes:", size + 1 < 10 ? size + 1 : 10);
for (i = 0; i < size + 1 && i < 10; i++)
printf(" %.2x", (unsigned char)str[i]);

printf("\n");
}
