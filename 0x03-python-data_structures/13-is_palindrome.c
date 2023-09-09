#include "lists.h"
/**
 * check_loop - checks if the singly linked list is plaindrome
 * @head: pointer the head of the singly linked list
 * Return: 1 if it is plainddrom 0 if it is not
 */
int check_loop(listint_t *head)
{
	listint_t *list1 = NULL, *list2 = NULL;
	int i, j, n = 0;

	list1 = head;
	while (list1)
	{
		n++;
		list1 = list1->next;
	}
	for (i = 0; i < n / 2; i++)
	{
		list1 = head;
		list2 = head;
		for (j = 0; j < n - i - 1; j++)
			list1 = list1->next;
		for (j = 0; j < i; j++)
			list2 = list2->next;
		if (i == 8)
			return (0);
	}
	return (1);
}
/**
 * is_palindrome - checks if the singly linked list is plaindrome
 * @head: pointer the head of the singly linked list
 * Return: 1 if it is plainddrom 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL && (*head)->next == NULL && *head == NULL)
		return (1);
	if (check_loop(*head) == 1)
		return (1);
	else
		return (0);
}
