package main.java;

import java.util.Scanner;
import java.util.Arrays;

public class BinarySearch {

    public static void binarySearch(int[] my_list, int number) {

        int high = my_list.length - 1;
        int mid = high;

        while (my_list[mid] != number) {
            if (my_list[mid] < number) {
                mid = (high+mid) / 2;
            }

            else {
                high = mid;
                mid = high / 2;
            }
        }

        System.out.println(mid+1);
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter array length:");
        int size = input.nextInt();
        System.out.println("Enter array elems:");
        int my_list[] = new int[size];
        for (int i = 0; i<size; i++) {
            my_list[i] = input.nextInt();
        }

        System.out.println("Enter random number:");
        int number = input.nextInt();

        if (Arrays.asList(my_list).contains(Integer.valueOf(number))) {
            binarySearch(my_list, number);
        }

        else {
            System.out.println ("Enter the number exists in array:" );
            number = input.nextInt();
            binarySearch(my_list, number);
        }

    }
}