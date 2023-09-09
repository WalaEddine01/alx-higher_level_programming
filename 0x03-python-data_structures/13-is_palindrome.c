#include "lists.h"
/**
 * is_palindrome - checks if the singly linked list is plaindrome
 * @head: pointer the head of the singly linked list
 * Return: 1 if it is plainddrom 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *list1 = NULL, *list2 = NULL;
	int i, j, n = 0;

	if (head == NULL && (*head)->next == NULL && *head == NULL)
	{
		return (1);
	}
	list1 = *head;
	while (list1)
	{
		n++;
		list1 = list1->next;
	}
	for (i = 0; i < n / 2; i++)
	{
		list1 = *head;
		list2 = *head;
		for (j = 0; j < n - i - 1; j++)
			list1 = list1->next;
		for (j = 0; j < i; j++)
			list2 = list2->next;
		if (list1->n != list2->n)
			return (0);
		free(list1);
		free(list2);
	}
	return (1);
}
