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

def main():
    '''
    creating a test case and calling the assign partners function for 3 months of data
    '''
    jan_input = ["Althea Farrel", "Darlena Cone", "Gerard Ta", "Deja Denner", "Kanisha Kimrey", "Piper Barraza", "Kathey Cotner", "Coleman Wolfe", "Marge Hudgins", "Rosalie Wilt"]
    feb_input = ["Althea Farrel", "Darlena Cone", "Gerard Ta", "Deja Denner", "Kanisha Kimrey", "Piper Barraza", "Kathey Cotner", "Shayne Vessels", "Nona Moles", "Socorro Vandenberg"]
    mar_input = ["Althea Farrel", "Darlena Cone", "Gerard Ta", "Deja Denner", "Kanisha Kimrey", "Piper Barraza", "Cletus Mair", "Coleman Wolfe", "Marge Hudgins", "Rosalie Wilt"]

    print(create_pairs(jan_input))
    print("----------------------")
    print(create_pairs(feb_input))
    print("----------------------")
    print(create_pairs(mar_input))
    print("----------------------")

if __name__ == "__main__":
    main()