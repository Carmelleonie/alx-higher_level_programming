#include "lists.h"


/**
*list_len -  A function that compute the lenght of a list
*@head: the head of the list
*Return: The lenght of the list
*/

int list_len(listint_t **head)
{
	int len = 0;

	while (head != NULL && (*head)->next != NULL)
	{
		len++;
		(*head) = (*head)->next;
	}
	return (len);
}

int is_palindrome(listint_t **head)
{
	int len = list_len(head);
	int i = 0, j = 0;
	listint_t *first, *last;

	first = last = *head;
	while (i != len / 2)
	{
		for (j = 0; j < i; j++)
		{
			first = first->next;
		}
		for (j = 0; j < (len - (i + 1)); j++)
		{
			last = last->next;
		}
		if (first->n != last->n)
		{
			return (0);
		}
		i++;
	}
	return (1);
}
