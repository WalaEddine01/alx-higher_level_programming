#include "lists.h"
/**
 * is_palindrome - checks if the singly linked list is plaindrome
 * @head: pointer the head of the singly linked list
 * Return: 1 if it is plainddrom 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *list1 = *head, *list2 = *head, *prev = *head, *next = *head;

	if (head == NULL && (*head)->next == NULL && *head == NULL)
		return (1);
	while (list2 != NULL && list2->next != NULL)
	{
		list2 = list2->next->next;
		next = list1->next;
		list1->next = prev;
		prev = list1;
		list1 = next;
	}
	if (list2 != NULL)
		list1 = list1->next;
	while (prev != NULL && list1 != NULL)
	{
		if (prev->n != list1->n)
			return (0);
		prev = prev->next;
		list1 = list1->next;
	}
	return (1);
}
