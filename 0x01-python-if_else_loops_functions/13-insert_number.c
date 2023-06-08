#include "lists.h"

/**
  * insert_node - a ans value
  * @head: the head
  * @number: index of position for addition
  *Return: sucess or failure
  */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *node = *head, *ans;

ans = malloc(sizeof(listint_t));
if (ans == NULL)
return (NULL);
ans->n = number;

if (node == NULL || node->n >= number)
{
ans->next = node;
*head = ans;
return (ans);
}

while (node && node->next && node->next->n < number)
node = node->next;
ans->next = node->next;
node->next = ans;

return (ans);
}
