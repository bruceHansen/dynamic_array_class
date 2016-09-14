
class Array:

    def __init__(self, initial_size=10, chunk_size=5):
        self.data = []
        self.size = 0
        self.chunk_size = chunk_size
        for i in range(initial_size):
            self.data.append(None)

    def add(self, item):      

        self._check_increase()

        self.data[self.size] = item

        self.size += 1

    def insert(self, index, item):
           
            #check bounds and if I can increase
        if self._check_bounds(index):
            my_error = 'Error: {} is not within the bounds of the array'.format(int(index))
            return my_error

        self._check_increase()

            #set end of index
        end_list = len(self.data) - 1

            #copy items above it if no empty slots
        if self.data[int(index)] == None:
            self.data[int(index)] = item
        else:
            for i in range(end_list - int(index)):
                self.data[end_list - i] = self.data[end_list - i - 1]

            self.data[int(index)] = item

        self.size += 1

    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
        
            #check if in-bounds
        if self._check_bounds(index):
            my_error = 'Error: {} is not within the bounds of the array'.format(int(index))
            return my_error

        self.data[int(index)] = item
        
    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
        
        my_return = ''
        if self._check_bounds(index):
            my_return = 'Error: {} is not within the bounds of the array'.format(int(index))
        else:
            my_return = self.data[int(index)]

        print(my_return)
        return my_return

    def delete(self, index):
        '''Deletes the item at the given index, decreasing the allocated memory if needed.  Throws an exception if the index is not within the bounds of the array.'''

        if self._check_bounds(index):
            my_error = 'Error: {} is not within the bounds of the array'.format(int(index))
            return my_error

        for item in range(len(self.data) - int(index) - 1):
        	self.data[int(index) + item] = self.data[int(index) + item + 1]

        self._check_decrease()
        
        self.size -= 1
        
    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''

        if self._check_bounds(index1):
            my_error = 'Error: {} is not within the bounds of the array'.format(int(index1))
            return my_error
        
        if self._check_bounds(index2):
            my_error = 'Error: {} is not within the bounds of the array'.format(int(index2))
            return my_error

        index_1 = self.data[int(index2)]
        index_2 = self.data[int(index1)]

        self.set(int(index2), index_2)
        self.set(int(index1), index_1)

    def _check_increase(self):
        '''
        Checks whether the array is full and needs to increase by chunk size
        in preparation for adding an item to the array.
        '''

        if self.size == len(self.data):
            self.alloc()

    def _check_decrease(self):
        '''
        Checks whether the array has too many empty spots and can be decreased by chunk size.
        If a decrease is warranted, it should be done by allocating a new array and copying the
        data into it (don't allocate multiple arrays if multiple chunks need decreasing).
        '''
            #check how many nones exist in the array
        indexes = []
        none_count = 0
        for i in range(len(self.data)):
            if self.data[i] != None:
                indexes.append(self.data[i])
            else:
                none_count += 1

            #if five or more 'None' found, then copy the array into new array
        if none_count > 4:
        	
            self.data = []

            for i in range(len(indexes)):
                self.data.append(None)

            for i in range(len(indexes)):
                self.data[i] = indexes[i]  

#            if self.size > 5:
 #               self.size -= self.chunk_size
        else:
            return True

    def _check_bounds(self, index):
        '''Ensures the index is within the bounds of the array: 0 <= index <= size.'''
        error = False

        if int(index) < 0:
            error = True

        elif int(index) >= self.size:
            error = True
        
        if error:
            return True

    def debug_print(self):

        string = ', '.join(map(str, self.data))

        my_debug = '{} of {} >>> {}'.format(self.size, len(self.data), string)
        print(my_debug)
        return my_debug

    ########## utilities ##########
    def alloc(self):
        for i in range(self.chunk_size):
            self.data.append(None)

