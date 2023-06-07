#include "lists.h"

/**
 * check_cycle - is there a cycle in the linked list
 *@list: the singly linked list
 *Return: success or failure
 */
int check_cycle(listint_t *list)
{
	listint_t *a2;
	listint_t *prev;
	
	a2 = list;
	prev = list;
	while (list && a2 && a2->next)
	{
		list = list->next;
		a2 = a2->next->next;

		if (list == a2)
		{
			list = prev;
			prev = a2;
			while (1)
			{
				a2 = prev;
				while (a2->next != list && a2->next != prev)
				{
					a2 = a2->next;
				}
				if (a2->next == list)
				{
					break;
				}
				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
