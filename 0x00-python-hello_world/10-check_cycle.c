#include "lists.h"
/**
 * check_cycle - detect cycle in single linked list
 * @list: single linked list
 * Return: 0 (no cycle) 1 (has cycle)
 */
int check_cycle(listint_t *list)
{
	const listint_t *slow, *fast;

	slow = list;
	fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
