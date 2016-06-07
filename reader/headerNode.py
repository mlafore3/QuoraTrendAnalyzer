class headNode:

# This is a dummy variable to represent 
# each coloumn heading as you iterate 
# through the items


    def __init__(self, name, typ):
        self.name = name
        #splice = typ.find('/SENSITIVE')
        
        #if splice >= 0:
            #self.type = typ[:splice]
            #self.restricted = True
       # else:
            #self.type = typ
            #self.restricted = False
        self.data = None
        self.type = typ 
        
    def __str__(self, includeData=False):
        output = '\nName:\t' + self.name + '\n'
        output += 'Type:\t' + self.type + '\n'
       # output += 'Restricted:\t' + str(self.restricted) + '\n'
        if includeData:
            if self.data:
                output += 'Data:\n' + self.data + '\n'
        return output
