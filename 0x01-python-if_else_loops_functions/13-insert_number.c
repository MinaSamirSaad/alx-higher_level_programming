#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - insert node ascending order with value number
 * @head: head pointer
 * @number: value
 * Return: address of inserted node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *nw;

	nw = malloc(sizeof(listint_t));

	if (nw == NULL)
		return (NULL);

	nw->n = number;
	nw->next = NULL;
	current = *head;
	while (current && current->next && current->next->n <= number)
	{
		current = current->next;
	}
	if (current == NULL)
	{
		*head = nw;
	}
	else if (current->n > number)
	{
		nw->next = current;
		*head = nw;
	}
	else
	{
		nw->next = current->next;
		current->next = nw;
	}
	return (nw);
}
