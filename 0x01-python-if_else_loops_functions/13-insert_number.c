#include "lists.h"
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly-linked list
 * @head: A double pointer the head node of the linked list
 * @number: The number to be inserted
 * Return: pointer to address of new node, NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nodelist = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (nodelist == NULL || nodelist->n >= number)
	{
		new->next = nodelist;
		*head = new;
		return (new);
	}

	while (nodelist && nodelist->next && nodelist->next->n < number)
		nodelist = nodelist->next;

	new->next = nodelist->next;
	nodelist->next = new;

	return (new);
}
