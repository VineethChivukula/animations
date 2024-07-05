// TC: O(n)
// SC: O(1)

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class Solution {

    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false;
        }

        ListNode s = head, f = head.next;
        while (s != f) {
            if (f == null || f.next == null) {
                return false;
            }
            s = s.next;
            f = f.next.next;
        }
        return true;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        ListNode head = new ListNode(3);
        head.next = new ListNode(2);
        head.next.next = new ListNode(0);
        head.next.next.next = new ListNode(-4);
        head.next.next.next.next = head.next;
        System.out.println(sol.hasCycle(head));
    }
}
