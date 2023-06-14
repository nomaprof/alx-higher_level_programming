#include "lists.h"

/**
 * reverse - reverse the second half
 *
 * @h_r: beginning of second half
 * Return: no value
 */
void reverse(listint_t **h_r)
{
    listint_t *prv;
    listint_t *crr;
    listint_t *nxt;

    prv = NULL;
    crr = *h_r;

    while (crr != NULL)
    {
        nxt = crr->next;
        crr->next = prv;
        prv = crr;
        crr = nxt;
    }

    *h_r = prv;
}

/**
 * compare - comparison of data
 *
 * @h1: beginning of first half
 * @h2: beginning of second half
 * Return: Success or Failure
 */
int compare(listint_t *h1, listint_t *h2)
{
    listint_t *hold1;
    listint_t *hold2;

    hold1 = h1;
    hold2 = h2;

    while (hold1 != NULL && hold2 != NULL)
    {
        if (hold1->n == hold2->n)
        {
            hold1 = hold1->next;
            hold2 = hold2->next;
        }
        else
        {
            return (0);
        }
    }

    if (hold1 == NULL && hold2 == NULL)
    {
        return (1);
    }

    return (0);
}

/**
 * is_palindrome - finds out if list is a palindrome
 * @head: points to the beginning of list
 * Return: success or failure
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *prev_slow;
    listint_t *scn_half, *halfway;
    int ans;

    slow = fast = prev_slow = *head;
    halfway = NULL;
    ans = 1;

    if (*head != NULL && (*head)->next != NULL)
    {
        while (fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;
            prev_slow = slow;
            slow = slow->next;
        }

        if (fast != NULL)
        {
            halfway = slow;
            slow = slow->next;
        }

        scn_half = slow;
        prev_slow->next = NULL;
        reverse(&scn_half);
        ans = compare(*head, scn_half);

        if (halfway != NULL)
        {
            prev_slow->next = halfway;
            halfway->next = scn_half;
        }
        else
        {
            prev_slow->next = scn_half;
        }
    }

    return (ans);
}
