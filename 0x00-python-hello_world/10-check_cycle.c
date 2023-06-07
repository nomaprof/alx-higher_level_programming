#include "lists.h"

/**
 * check_cycle - is there a cycle in the linked list
 *@list: the singly linked list
 *Return: success or failure
 */
int check_cycle(listint_t *list)
{
	listint_t *a1 = NULL, *a2 = NULL;

	a1 = a2 = list;
	while (list && a1 && a2 && a1->next && a2->next)
	{
		a1 = a1->next;
		a2 = a2->next->next;
		if (!a2 || !a1)
		{
			return (0);
		}
		if (s2->next == s1)
		{
			return (1);
		}
	}
	return (0);
}
