'''
Concept: OOP
Mini Project - OOP Chat System
Let's create a Chat System using OOPs concepts. We have to create classes:
User
Message
ChatRoom
And we have to implement functions:
sending messages
viewing chat history
user joining and leaving the chatroom
'''
class Message:
    message_counter = 1

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content #stores the message text
        self.id = Message.message_counter #tracking message
        Message.message_counter += 1

    def __str__(self):
        return f"({self.id}) {self.sender.username}: {self.content}"


class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None #None to indicate absence

    def join_chatroom(self, chatroom): #method to add user to a room
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom #update the user in chartroom
            print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self): #checks whether the user is currently not in a chatroom.
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None

    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message (not in chatroom)")
        else:
            self.chatroom.broadcast(self, content)


class ChatRoom: #holds users and messages
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    #creats a message and distributes
    def broadcast(self, sender, content):
        msg = Message(sender, content)
        self.messages.append(msg) #save the message in chart history
        print(msg)

    def show_chat_history(self):
        print(f"\nChat History of {self.name}:")
        for msg in self.messages: #for loop is used for reading every letter one by one
            print(msg)


if __name__ == "__main__":
    room = ChatRoom("Python Language")

    u1 = User("Alice")
    u2 = User("Bob")
    u3 = User("Charlie")

    u1.join_chatroom(room)

    u1.send_message("Hello everyone!")
    u2.send_message("Hi Alice!")

    u3.join_chatroom(room)
    u3.send_message("Hey guys what's up ?")

    room.show_chat_history()

    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom()




