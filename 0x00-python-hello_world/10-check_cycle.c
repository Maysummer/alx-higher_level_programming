#include "lists.h"
/**
 * check_cycle - check if a singly linked list has a cycle in it
 * @list: list
 * Return: 0 (no cycle), 1 (cycle)
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (!list)
		return (0);
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
