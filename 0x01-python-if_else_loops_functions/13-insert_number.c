#include <stddef.h>
#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - function that inserts a number into a sorted singly linked list
 * @head: double pinter to list
 * @number: number of new node
 * Return: address of new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *current = *head;
	listint_t *old = NULL;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head && ((*head)->n > number)) /*add to start*/
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (current && (current->n < number))
	{
		old = current;
		current = current->next;
	}
	old->next = new;
	new->next = current;
	return (new);
}
