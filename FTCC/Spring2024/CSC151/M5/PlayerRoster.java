/* this is a menu driven program to manage a team of 5
   02/15/2024
   CSC151 - Java
   Harley Coughlin

   extra note: methods aren't available until next module
*/

import java.util.Scanner;

public class PlayerRoster {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);

        int[][] players = new int[5][2];
        int i, j, newJersey, newRating, playerJersey;
        boolean keepGoing = true, notFound = true;
        String option;

        for (i = 0; i < 5; ++i) {
            System.out.println("Enter player " + (i + 1) + "'s jersey number:");
            players[i][0] = scnr.nextInt();

            System.out.println("Enter player " + (i + 1) + "'s rating:");
            players[i][1] = scnr.nextInt();
            System.out.println();
        }

        System.out.println("ROSTER");

        for (i = 0; i < 5; ++i) {
            System.out.print("Player " + (i + 1) + " -- Jersey number: ");
            System.out.println(players[i][0] + ", Rating: " + players[i][1]);
        }

        while (keepGoing) {
            System.out.println();
            System.out.println("MENU");
            System.out.println("u - Update player rating");
            System.out.println("a - Output players above a rating");
            System.out.println("r - Replace player");
            System.out.println("o - Output roster");
            System.out.println("q - Quit");
            System.out.println();

            System.out.print("Choose an option:");
            option = scnr.next();
            System.out.println();

            notFound = true;
            i = 0;
            switch (option) {
                case "u":
                System.out.println("Enter a jersey number:");
                playerJersey = scnr.nextInt();

                while (notFound) {
                    if (players[i][0] != playerJersey && i < 4) {
                        ++i;
                    } else if (players[i][0] == playerJersey) {
                        System.out.println("Enter a new rating for player:");
                        newRating = scnr.nextInt();
                        players[i][1] = newRating;
                        notFound = false;
                    } else {
                        System.out.println("Player jersey not found\n");
                        break;
                    }
                }
                break;

                case "a":
                System.out.println("Enter a rating:");
                // no point in making a rating variable if this one isn't being used
                newRating = scnr.nextInt();

                System.out.println("ABOVE " + newRating);
                for (i = 0; i < 5; ++i) {
                    if (players[i][1] > newRating) {
                        System.out.print("Player " + (i + 1) + " -- Jersey number: ");
                        System.out.println(players[i][0] + ", Rating: " + players[i][1]);
                    }
                }
                break;

                case "r":
                System.out.println("Enter a jersey number:");
                playerJersey = scnr.nextInt();

                while (notFound) {
                    if (players[i][0] != playerJersey && i < 4) {
                        ++i;
                    } else if (players[i][0] == playerJersey) {
                        System.out.println("Enter a new jersey number:");
                        newJersey = scnr.nextInt();
                        System.out.println("Enter a rating for the new player:");
                        newRating = scnr.nextInt();
                        players[i][0] = newJersey;
                        players[i][1] = newRating;
                        notFound = false;

                    } else {
                        System.out.println("Jersey number not found\n");
                        break;
                    }
                }
                break;

                case "o":
                System.out.println("ROSTER");

                for (i = 0; i < 5; ++i) {
                    System.out.print("Player " + (i + 1) + " -- Jersey number: ");
                    System.out.println(players[i][0] + ", Rating: " + players[i][1]);
                }
                break;

                case "q":
                keepGoing = false;
                break;

                default:
                System.out.println("Please select a menu option");
            }
        }
    }
}
