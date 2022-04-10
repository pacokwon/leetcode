use std::collections::BinaryHeap;

struct Solution;

impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        let mut heap = BinaryHeap::from(stones);

        while heap.len() > 1 {
            let max1 = heap.pop().unwrap();
            let max2 = heap.pop().unwrap();

            if max1 > max2 {
                heap.push(max1 - max2);
            }
        }

        if let Some(stone) = heap.pop() {
            stone
        } else {
            0
        }
    }
}

fn main() {
    println!("{}", Solution::last_stone_weight(vec![1, 1]));
}
