#CAPITULO 1
#centralidade de grau , grafos

users =[
{"id": 0, "name": "Hero"},
{"id": 1, "name": "Dunn"},
{"id": 2, "name": "Sue"},
{"id": 3, "name": "Chi"},
{"id": 4, "name": "Thor"},
{"id": 5, "name": "Clive"},
{"id": 6, "name": "Hicks"},
{"id": 7, "name": "Devin"},
{"id": 8, "name": "Kate"},
{"id": 9, "name": "Klein"} 
] 

friendship_pairs = [
(0, 1),(0, 2),(1, 2),(1, 3),(2, 3),(3, 4),
(4, 5),(5, 6),(5, 7),(6, 8),(7, 8),(8, 9)
]


#inicialize o dict com uma lista vazia para cada ID de usuário:
friendships = {user["id"]: [] for user in users}

#em execute um loop pelos pares de amigos para preencher o dict:
for i, j in friendship_pairs:
    friendships[i].append(j)  # adicione j como amigo de i
    friendships[j].append(i)  # adicione i como amigo de j
    
    
#TOTAL DE CONEXOES SOMANDO O TAMANHO DE TODAS AS LISTAS DE FRIENDS    
def number_of_friends(user):
    """quantos amigos o usuário tem?"""
    user_id = user["id"]
    friends_id = friendships[user_id]
    return len(friends_id)

total_connections = sum(number_of_friends(user)for user in users)

#MEDIA

num_users = len(users)
avg_connections = total_connections / num_users

#Crie uma lista (user_id e number_of_friends)
num_friends_by_id = [[user["id"], number_of_friends(user)] for user in users]

#ordena de forma decrescente
num_friends_by_id.sort(key=lambda x: x[1], reverse=True)

#friend id



#caminhando pelo grafo, amigo do meu amigo

def foaf_ids_bad(users):
    return[[foaf_id for friends_id in friendships[users]]
           for foaf_id in friendships[friends_id] ]

print(friendships[0])
#
