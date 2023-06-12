#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - reverse single linked list
 * @head: head of single linked list
 * Return: new head (tail of old one)
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev, *curr, *nex;

	prev = NULL;
	nex = *head;
	while (nex)
	{
		curr = nex;
		nex = nex->next;
		curr->next = prev;
		prev = curr;
	}
	return (prev);
}

/**
 * is_palindrome - check if linked list is palindrom
 * @head: linked list
 * Return: 0 if not palindrome 1 is palindrome
 */
int is_palindrome(listint_t **head)
{
	int len_list = 0, i = 0, len_half, flag = 1;
	listint_t *current = *head, *other_half, *reversed_half;

	while (current)
	{
		len_list++;
		current = current->next;
	}
	if (len_list <= 1)
		return (1);

	len_half = len_list / 2;
	other_half = *head;
	while (i++ < len_half)
		other_half = other_half->next;
	if (len_list % 2)
		other_half = other_half->next;

	reversed_half = reverse_list(&other_half);
	other_half = reversed_half;

	current = *head;
	i = 0;
	while (i++ < len_half)
	{
		if (current->n != reversed_half->n)
		{
			flag = 0;
			break;
		}
		current = current->next;
		reversed_half = reversed_half->next;
	}

	reverse_list(&other_half);
	return (flag);
}
