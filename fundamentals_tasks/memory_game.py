
sequence = input().split()
moves = 0

while True:
    command = input()

    if command == "end":
        print(f"Sorry you lose :(\n{' '.join(sequence)}")
        break

    command = command.split()
    index1, index2 = int(command[0]), int(command[1])

    if index1 == index2 or index1 < 0 or index2 < 0 or index1 >= len(sequence) or index2 >= len(sequence):
        moves += 1
        mid_index = len(sequence) // 2
        new_element = f"-{moves}a"
        sequence.insert(mid_index, new_element)
        sequence.insert(mid_index, new_element)
        print("Invalid input! Adding additional elements to the board")
    else:
        moves += 1
        if sequence[index1] == sequence[index2]:
            matched_element = sequence[index1]
            if index1 > index2:
                sequence.pop(index1)
                sequence.pop(index2)
            else:
                sequence.pop(index2)
                sequence.pop(index1)
            print(f"Congrats! You have found matching elements - {matched_element}!")
        else:
            print("Try again!")

        if not sequence:
            print(f"You have won in {moves} turns!")
            break


# List < string > list = Console.ReadLine().Split().ToList();
#
# string
# input = string.Empty;
# int
# counter = 0;
# bool
# end = false;
# while ((input=Console.ReadLine()) != "end")
# {
#     string[]
# command = input.Split();
# string
# firstIndex = command[0];
# string
# secondIndex = command[1];
# int
# startIndex = int.Parse(firstIndex);
# int
# endIndex = int.Parse(secondIndex);
# if (list.Count == 0 | | list.Count == 1)
# {
#     end = true;
# Console.WriteLine($"You have won in {counter} turns!");
# break;
# }
# if (startIndex < 0 | | startIndex >= list.Count)
# {
# Console.WriteLine("Invalid input! Adding additional elements to the board");
# counter + +;
# string
# added = "-" + counter + "a";
# list.Insert(list.Count / 2, added);
# list.Insert(list.Count / 2, added);
#
# }
# else if (endIndex < 0 | | endIndex >= list.Count)
# {
# Console.WriteLine("Invalid input! Adding additional elements to the board");
# counter + +;
# string
# added = "-" + counter + "a";
# list.Insert(list.Count / 2, added);
# list.Insert(list.Count / 2, added);
#
# }
# else if (startIndex == endIndex)
# {
# Console.WriteLine("Invalid input! Adding additional elements to the board");
# counter + +;
# string
# added = "-" + counter + "a";
# list.Insert(list.Count / 2, added);
# list.Insert(list.Count / 2, added);
# }
# else
# {
#
# counter + +;
# if (list[startIndex] == list[endIndex])
#     {
#         Console.WriteLine($"Congrats! You have found matching elements - {list[startIndex]}!");
#     if (firstIndex == "0")
#     {
#     list.Remove(list[startIndex]);
#     list.Remove(list[endIndex-1]);
#     }
#     else
#     {
#     list.Remove(list[startIndex]);
#     list.Remove(list[endIndex]);
#     }
#
#     }
#     else Console.WriteLine("Try again!");
# }
# }
# if (end == false)
# {
# Console.WriteLine($"Sorry you lose :(");
# Console.WriteLine(String.Join(" ", list));

