'''
Ethan Ash
2/2/2020
'''
import random

past_pairs = {}

def create_pairs(people):
    '''
    returns a list of arrays of length 2 containing unique pairs
    '''
    final_pairs = []

    people_to_be_paired = random.sample(people, len(people))

    while len(people_to_be_paired) > 0:    
        if len(people_to_be_paired) == 1:
            print("Odd number of people. No partner found for " + people_to_be_paired[0])
            break
        first_person_index = None
        i = 0
        first_person_to_pair = None
        possible_second_person_to_pair = None
        possible_second_person_index = None
        second_lowest_pairs = float('inf')
        lowest_pairs = float('inf')
        #choose the person with the least possible number of connections
        for person in people_to_be_paired:
            if person in past_pairs:
                conflicting_pairs = 0
                for past_partner in past_pairs[person]:
                    if past_partner in people_to_be_paired:
                        conflicting_pairs += 1
                possible_pairs = len(people_to_be_paired)-conflicting_pairs-1
                if possible_pairs < lowest_pairs:
                    second_lowest_pairs = lowest_pairs
                    possible_second_person_to_pair = first_person_to_pair
                    possible_second_person_index = first_person_index

                    first_person_to_pair = person
                    lowest_pairs = possible_pairs
                    first_person_index = i
                elif possible_pairs < second_lowest_pairs:
                    possible_second_person_to_pair = person
                    second_lowest_pairs = possible_pairs
                    possible_second_person_index = i
            else:
                possible_pairs = len(people_to_be_paired)-1
                if possible_pairs < lowest_pairs:
                    second_lowest_pairs = lowest_pairs
                    possible_second_person_to_pair = first_person_to_pair
                    possible_second_person_index = first_person_index

                    first_person_to_pair = person
                    lowest_pairs = possible_pairs
                    first_person_index = i
                elif possible_pairs < second_lowest_pairs:
                    possible_second_person_to_pair = person
                    second_lowest_pairs = possible_pairs
                    possible_second_person_index = i
            i += 1

        #find the best suitable partner for the chosen person
        second_person_index = None
        j = 0
        second_person_to_pair = None
        if not first_person_to_pair in past_pairs:
            second_person_to_pair = possible_second_person_to_pair
            second_person_index = possible_second_person_index
        elif not possible_second_person_to_pair in past_pairs[first_person_to_pair]:
            second_person_to_pair = possible_second_person_to_pair
            second_person_index = possible_second_person_index
        else:
            lowest_pairs = float('inf')
            for person in people_to_be_paired:
                if not person in past_pairs[first_person_to_pair] and person != first_person_to_pair:
                    if person in past_pairs:
                        conflicting_pairs = 0
                        for past_partner in past_pairs[person]:
                            if past_partner in people_to_be_paired:
                                conflicting_pairs += 1
                        possible_pairs = len(people_to_be_paired)-conflicting_pairs-1
                        if possible_pairs < lowest_pairs:
                            second_person_to_pair = person
                            lowest_pairs = possible_pairs
                            second_person_index = j
                j += 1
        if second_person_to_pair is None:
            print("found no person to pair with " + first_person_to_pair)
            del people_to_be_paired[first_person_index]
            continue
        
        final_pairs.append([first_person_to_pair, second_person_to_pair])

        if first_person_to_pair in past_pairs:
            past_pairs[first_person_to_pair].append(second_person_to_pair)
        else:
            past_pairs[first_person_to_pair] = [second_person_to_pair]
        
        if second_person_to_pair in past_pairs:
            past_pairs[second_person_to_pair].append(first_person_to_pair)
        else:
            past_pairs[second_person_to_pair] = [first_person_to_pair]
        
        if first_person_index > second_person_index:
            del people_to_be_paired[first_person_index]
            del people_to_be_paired[second_person_index]
        else:
            del people_to_be_paired[second_person_index]
            del people_to_be_paired[first_person_index]

    return final_pairs

def printPairs(pairArray):
    for pairing in pairArray:
        print(pairing[0] + " + " + pairing[1])

def main():
    '''
    allowing user to create groups to partner or creating a test case
    '''

    input_one = ["Althea Farrel", "Darlena Cone", "Gerard Ta", "Deja Denner", "Kanisha Kimrey", "Piper Barraza", "Kathey Cotner", "Coleman Wolfe", "Marge Hudgins", "Rosalie Wilt"]
    input_two = ["Althea Farrel", "Darlena Cone", "Gerard Ta", "Deja Denner", "Kanisha Kimrey", "Piper Barraza", "Kathey Cotner", "Shayne Vessels", "Nona Moles", "Socorro Vandenberg"]
    input_three = ["Althea Farrel", "Darlena Cone", "Gerard Ta", "Deja Denner", "Kanisha Kimrey", "Piper Barraza", "Cletus Mair", "Coleman Wolfe", "Marge Hudgins", "Rosalie Wilt"]

    examples = [input_one, input_two, input_three]
    index = 0

    loop = True
    while loop:
        user_input = input("Enter the names of people that you want grouped in this round (first and last name), seperated by a comma and a space, or type \"test\" to use a test sample: \n")
        input_array = []
        if user_input == "test":
            input_array = examples[index]
        else:
            input_array = user_input.split(", ")
        
        printPairs(create_pairs(input_array))
        wait = input("To do another round, type \"Y\". To quit, type \"N\".\n")
        if wait == "N":
            loop = False
        index += 1 
        index = index % 3

if __name__ == "__main__":
    main()
