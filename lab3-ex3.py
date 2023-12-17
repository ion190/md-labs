# 3. Matrix
# You have a set of 20 people connected via a friendship matrix. The whole list is given in matrix.txt..
# 3.1 Friends
# Find the person with the most friends.
# 3.2 Sort
# Sort all the people by the number of friends.
# 3.3 Let's do ratings
# How to do that? Well, each person in the graph is connected to everyone else at some level. Therefore, each person will have a list of connections which is as long as the total list of people in the graph (in our case, 20). You then have to compute the shortest path from each of the nodes to each of the other nodes.
# For example, let’s say that you found that from node 0 you can reach node 3 in 5 steps (that is, the shortest path connecting nodes 0 and 3 has 5 steps). That means that node 3 will be a connection of level 5 to node 0 and will therefore contribute to 0 with 4 points.
# As a procedure, you can take each item n and then compute the distances between n and all the other vertices of the graph. You can use these distances to compute the value that is added by each of the other n − 1 vertices to n. Sum it and you’ll have the value of vertex n.
# In order to find the shortest path between two vertices, you’ll have to use Dijkstra's algorithm. You can find plenty of implementations of that algorithm online.
# Compute the points for each person in our network. Let’s call it ”Rating”
# 3.4 Influential people
# Let’s say that each of these people has a certain rate of posting content. Obviously, people who communicate more are much more influential. Suppose that you need to promote a new brand using social media. We found out how often each of these 20 people writes something on their walls. You can find it in influence.txt
# Whom of these people will you contact? Why? Be advised that not only the frequency of posting matters, but also the number of friends!
# Use the data from the previous exercise and find the new ”Rating” for each person by multiplying it with 0.5 of the posting rate.
# Please sort the people by the newly computed rating.
# 3.5 Analyse your content
# You are publishing a book and would like to promote it through the use of social media. The book’s title is ”From T-Rex to Multi Universes: How the Internet has Changed Politics, Art and Cute Cats.” You have done some research in the world’s most popular social network and have found that the range of interests is stored in interests.txt
# Analyse your title and see what spectre of interests is your book marketable to.
# 3.6 Promote it
# We have provided you with a list of interests of each of these people. You can find it in interests.txt.
# Considering the set of interests you have chosen, who of them would you market the book to? Let’s say that a person has 5 of her interests coinciding with your books and she has a Rating of 346. Multiply her rating with the 0.2 * coinciding interests to see a final score. Sort the people by this final score.
# Provide us with a list of 5 people we should contact to make your book a bestseller! Please use the names found in people_interests.txt.


def adjacency_matrix_to_set(matrix):
    adjacency_set = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                adjacency_set.append([i,j,1])

    return adjacency_set

def read_matrix(file_path):
    with open(file_path,"r") as file:
        text=file.readline()
        lines=file.readlines()
    names=[element.strip() for element in text.split("|")]
    matrix=[list(map(int,(line.split("|")[1].strip().replace(" ","")))) for line in lines]

    return names, matrix

def read_influence(file_path):
    with open(file_path,"r") as file:
        lines=file.readlines()
    for i in range(len(lines)):
        lines[i] = [element.strip() for element in lines[i].strip().split(":")]
    dict={element[0]:float(element[1]) for element in lines}
    return dict

def read_interests(file_path):
    with open(file_path,"r") as file:
        lines=file.read().split('\n')


    return lines


def read_people_interests(file_path):
    with open(file_path,"r") as file:
        lines=file.readlines()
    for i in range(len(lines)):
        lines[i] = [element.strip() for element in lines[i].strip().split(":")]
    dict={element[0]:element[1].split() for element in lines}
    return dict


#CODE FOR PROBLEM 3,1

names,friendship_matrix=read_matrix("matrix.txt")
names_dict={names[i]:sum(friendship_matrix[i]) for i in range(20)}
print("PROBLEM 3.1:")
print("{0} has the most friends, {1} friends".format(max(names_dict,key=names_dict.get),names_dict[max(names_dict,key=names_dict.get)]))

#CODE FOR PROBLEM 3,2

sorted_names=dict(sorted(names_dict.items(), key=lambda item: item[1]))
print("\n\nPROBLEM 3.2:")
for name, friends in sorted_names.items():
    print("{0} has {1} friends".format(name,friends))

#CODE FOR PROBLEM 3,3

friendship_list=adjacency_matrix_to_set(friendship_matrix)
rating={name:0 for name in names}
for start in range(len(names)):
    connections = [float("inf") for _ in range(len(names))]
    connections[start] = 0

    for _ in range(len(names)-1):
                temp_connections = list(connections)
                for source, dest, connection in friendship_list:
                    connection_degree = connections[source] + connection
                    if connection_degree < temp_connections[dest]:
                        temp_connections[dest] = connection_degree
                connections = temp_connections

    connections.pop(start)
    rating[names[start]]=sum(connections)-len(names)+1
print("\n\nPROBLEM 3.3:")
print(rating)


#CODE FOR PROBLEM 3,4


print("\n\nPROBLEM 3.4")
posting_rate=read_influence("influence.txt")
posting_friends={name:0.5*posting_rate[name]+0.5*names_dict[name] for name in names}
print("By frequency and friends criteria I will contact {0} because he has an average score of {1} ".format(max(posting_friends,key=posting_friends.get),posting_friends[max(posting_friends,key=posting_friends.get)]))
new_rating={name:0.5*posting_rate[name]*rating[name] for name in names}
sorted_rating=dict(sorted(new_rating.items(), key=lambda item: item[1]))
print("\nNew Rating based on Connections and Posting Rate:")
for name, score in sorted_rating.items():
    print("{0} has a score of {1} ".format(name,score))


#CODE FOR PROBLEM 3,5


print("\n\nPROBLEM 3.5")
interests=read_interests("interests.txt")
book_name="From T-Rex to Multi Universes How the Internet has Changed Politics Art and Cute Cats"
book_name=book_name.split(' ')
my_interests=[]
for interest in interests:
    if interest in book_name:
        my_interests.append(interest)
print('The book is marketable in the following spectre of interests: ',end='')
for interest in my_interests:
    print(interest,end=', ')
print()


#CODE FOR 3.6

print("\n\nPROBLEM 3.6")
people_interests=read_people_interests("people_interests.txt")
print(people_interests)
final_score={name:0.2*len(set(people_interests[name]).intersection(set(my_interests)))*new_rating[name] for name in names}
print(final_score)
sorted_final=dict(sorted(final_score.items(), key=lambda item: item[1]))
print("\nFinal Results:")
for name, score in sorted_final.items():
    print("{0} has a score of {1:.4f} ".format(name,score))
