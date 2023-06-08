#include "lists.h"

/**
  * insert_node - a ans value
  * @head: the head
  * @number: index of position for addition
  *Return: sucess or failure
  */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *ans;
    listint_t *h;
    listint_t *h_before;

    h = *head;
    ans = malloc(sizeof(listint_t));

    if (ans == NULL)
        return (NULL):

    while (h != NULL)
    {
        if (h->n > number)
            break;
        h_before = h;
        h = h->next;
    }

    ans->n = number;

    if (*head == NULL)
    {
        ans->next = NULL;
        *head = ans;
    }
    else
    {
        ans->next = h;
        if (h == *head)
            *head = ans;
        else
            h_before->next = ans;
    }
    return (ans);
}
