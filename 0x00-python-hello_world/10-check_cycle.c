#include "lists.h"
/**
 * check_cycle - check if a singly linked list has a cycle in it
 * @list: list
 * Return: 0 (no cycle), 1 (cycle)
 */

int check_cycle(listint_t *list)
{
	listint_t *arr[1024];
	int i, len = 0;

	while (list)
	{
		i = 0;
		while (i < len)
		{
			if (arr[i] == list)
				return (1);
			i++;
		}
		arr[len] = list;
		len++;
		list = list->next;
	}
	return (0);
}
