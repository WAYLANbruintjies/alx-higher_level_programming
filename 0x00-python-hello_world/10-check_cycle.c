#include "lists.h"

/**
 * check_cycle - Checks to see if a linked list has a cycle
 * @list: the linked list to be computed
 * Return: 1 for cycle, 0 for no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *low = list;
	listint_t *high = list;

	if (!list) /* if list is empty */
		return (0);

	while (low && high && high->next)
	{
		low = low->next;
		high = high->next->next;
		if (low == high)
			return (1);
	}

	return (0);
}

