#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 * Description: checks if a singly linked list has a cycle in it
*/
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL && list->next == NULL && list->next->next == NULL)
		return (0);
	slow = list;
	fast = list;
	while (fast && slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
