#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

listint_t *reverse_listint(listint_t **head);

/**
 * reverse_listint - Reverse a linked list
 * @head: pointer to the start node of the list
 * Return: pointer to the head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *nodenew = *head, *next, *prev = NULL;

	while (nodenew) /* while TRUE */ /* not NULL */
	{
		next = nodenew->next;
		nodenew->next = prev;
		prev = nodenew;
		nodenew = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: pointer to the first part of the node
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev_, *new;
	size_t size = 0, len;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp) /* while temp is true */
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (len = 0; len < (size / 2) - 1; len++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev_ = reverse_listint(&tmp);
	new = rev_;

	tmp = *head;
	while (rev_)
	{
		if (tmp->n != rev_->n)
			return (0);
		tmp = tmp->next;
		rev_ = rev_->next;
	}
	reverse_listint(&new);

	return (1);
}
