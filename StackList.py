class Node:
    def __init__(self, data):
        self._data = data
        self._next = None
        self._prev = None


class StackList:
    def __init__(self):
        self.stack_data = list()

    def push(self, new_data):
        self.stack_data.append(new_data)

    def top(self):
        if len(self.stack_data) == 0:
            return None
        else:
            return self.stack_data[-1]

    def pop(self):
        if len(self.stack_data) == 0:
            return None
        else:
            pop_data = self.stack_data.pop()
            return pop_data

    def size(self):
        return len(self.stack_data)


class UndoRedo:
    def __init__(self):
        self.mainStack = StackList()  # stack ini sebagai tempat menyimpan data pertama kali
        # stack ini sebagai tempat menyimpan data yang di hapus
        self.backupStack = StackList()

    # def write(self, data):
    # Tuliskan Code Anda Disini
    def undo(self):
        x = self.pointer
        self.pop()
        print(x)

    # Tuliskan Code Anda Disini
    def redo(self):
        # Tuliskan Code Anda Disini
        x = self.pointer.prev
        if x is None:
            print("nothing to redo")
        else:
            self.push(x)
            print(x)

    # def printInfo(self):
    #     if self._size == 0:
    #         return "Empty"
    #     else:


if __name__ == "__main__":
    obj_undoredo = UndoRedo()
    obj_undoredo.undo()
    obj_undoredo.redo()
    obj_undoredo.write("Pada Suatu Hari hiduplah seorang kakek-kakek")
    obj_undoredo.write("Dia tinggal sebatang kara di pegunungan")
    obj_undoredo.write("Dia kemudian tutun gunung buat kulaih")
    obj_undoredo.write("SEMESTER 5 BANYAK TUGAS!!!")
    obj_undoredo.printInfo()
    obj_undoredo.undo()
    obj_undoredo.undo()
    obj_undoredo.undo()
    obj_undoredo.undo()
    obj_undoredo.redo()
    obj_undoredo.redo()
    obj_undoredo.redo()
