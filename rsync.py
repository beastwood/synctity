'''
Copyright 2009, 2010 Brian S. Eastwood.

This file is part of Synctus.

Synctus is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Synctus is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Synctus.  If not, see <http://www.gnu.org/licenses/>.

Created on Nov 9, 2009
'''
import commands

class Path:
    ''' 
    Represents a fully qualified network path name as recognized by rsync.  
    This includes a user, host, and path. An rsync path is printed as:
        user@host:path.
    '''
    def __init__(self, path='', host='', user=''):
        ''' Initialize a network path ''' 
        self.user = user
        self.host = host
        self.path = path
    
    def __str__(self):
        ''' Build the full network path string'''
        str = ''
        if self.user != '':
            str = str + self.user + "@"
            
        if self.host != '':
            str = str + self.host + ":"
        elif self.user != '':
            str = str + "localhost:"
        
        str = str + self.path
        
        if (str == ''):
            str = '.'
        
        return str

    def getUser(self): return self.user
    def setUser(self, value): self.user = value
    def getHost(self): return self.host
    def setHost(self, value): self.host = value
    def getPath(self): return self.path
    def setPath(self, value): self.path = value
    
class Option:
    '''
    Represents an option in the rsync command.  Options can either be 
    short-style options, like -v, or long-style options, like --verbose.  
    Both option styles can have parameters, like -e 'ssh -p 2234' or 
    --exclude=pattern.
    
    Options are stored in a dictionary with (key, [list of params]) entries.
    This approach is used because an rsync option can appear multiple times in 
    a single rsync command, e.g. --exclude=pathA --exclude=pathB.  In this
    example, there would be a single key for the --exclude option and two
    parameters to specify the paths.
    '''
    def __init__(self):
        self.options = dict()
        
    def __iter__(self):
        return self.options.__iter__()
        
    def enable(self, option, param=''):
        ''' Enable or turn on a flag.  The flag and optional parameter are
        added to the dictionary of options. '''
        if option in self.options:
            # the option is already in the list, 
            # so append the parameter if it is unique
            if not param in self.options[option]:
                self.options[option].append(param)
        else:
            # the option is new, so create an entry in a list
            self.options[option] = [param]
    
    def disable(self, option, param=None):
        ''' Disable or turn off a flag.  This removes the first option whose
        flag name matches.'''
        if option in self.options:
            if param == None:
                del self.options[option]
            elif param in self.options[option]:
                self.options[option].remove(param)
                if len(self.options[option]) == 0:
                    del self.options[option]
    
    def __str__(self):
        str = ''
        for opt in sorted(self.options):
            ostr = ''
            if len(opt) == 1:
                for param in self.options[opt]:
                    ostr = ostr + "-%s %s " % (opt, param)
            else:
                for param in self.options[opt]:
                    if len(param) > 0:
                        ostr = ostr + "--%s=%s " % (opt, param)
                    else:
                        ostr = ostr + "--%s " % opt
            
            str = str + " " + ostr.strip()
        return str.strip()
    
    def getOptions(self): return self.options
    def setOptions(self, value): self.options = value
    
class Command:
    '''
    An rsync command, which has the format:
        rsync OPTIONS SOURCE DESTINATION
    rsync commands can be run forwards or backwards (by swapping destination 
    and source).
    '''
    def __init__(self, srcPath=None, destPath=None, options=None):
        '''
        Initialize a command instance.
        '''
        # Big lesson learned here.  If you specify default parameters to a 
        # method, they are instantiated only once, when the define is read.
        # This has big implications for mutable arguments to __init__ methods, 
        # because every instance of the class will share the same init
        # parameters.  This can be a very bad thing if your class holds these
        # parameters as instance variables.
        if srcPath != None:
            self.source = srcPath
        else:
            self.source = Path()
        
        if destPath !=None:
            self.destination = destPath
        else:
            self.destination = Path()
            
        if options != None:
            self.options = options
        else:
            self.options = Option()
            self.options.enable('n')
        
    def forward(self):
        return "rsync %s %s %s" % (self.options, self.source, self.destination)
    
    def reverse(self):
        return "rsync %s %s %s" % (self.options, self.destination, self.source)
    
    def __str__(self):
        return self.forward()
    
    def execute(self, reverse=False):
        ''' Execute the rsync command and display the result.  The reverse
        option specifies whether this command should be run in forward or
        reverse order, with the default being forward.'''
        if (not reverse):
            print "Executing: " + self.forward()
            (status, output) = commands.getstatusoutput(self.forward())
        else:
            print "Executing: " + self.reverse()
            (status, output) = commands.getstatusoutput(self.reverse())
            
        print output
        
    def getSource(self): return self.source
    def setSource(self, value): self.source = value
    def getDestination(self): return self.destination
    def setDestination(self, value): self.destination = value
    def getOptions(self): return self.options
    def setOptions(self, value): self.options = value
    
    def getDescription(self):
        string = ''
        if self.getSource().getHost() != "":
            string = string + self.getSource().getHost() + ":"
        string = string + self.getSource().getPath() + " --> "
        if self.getDestination().getHost() != "":
            string = string + self.getDestination().getHost() + ":"
        string = string + self.getDestination().getPath()
        return string
        
class Profile:
    '''
    A collection of rsync commands.
    '''
    def __init__(self, name="NewProfile"):
        self.name = name
        self.commands = list()
        self.presync = ''
        self.postsync = ''
        
    def add(self, command):
        self.commands.append(command)
        
    def remove(self, index):
        if index < len(self.commands):
            self.commands.remove(self.commands[index])
    
    def get(self, index):
        if index < len(self.commands):
            return self.commands[index]
            
    def __iter__(self):
        return self.commands.__iter__()
    
    def execute(self, reverse=False):
        for command in self.commands:
            command.execute(reverse);
            
    def getName(self): return self.name
    def setName(self, value): self.name = value
    def getCommands(self): return self.commands
    
    # prebackup and postbackup were added later, so the get methods use getattr to 
    # avoid problems with old pickled Profile objects.
    def getPreSync(self): return getattr(self, 'presync', '')
    def getPostSync(self): return getattr(self, 'postsync', '')
    def setPreSync(self, value): self.presync = value
    def setPostSync(self, value): self.postsync = value
    
if __name__ == "__main__":
    
    path1 = Path()
    path2 = Path()
    path1.setPath("path1")
    path2.setPath("path2")
    print path1, path2
    
    command1 = Command()
    command2 = Command()
    command1.getSource().setPath("command1")
    command1.getOptions().enable("c1")
    print command1, command2
    command2.getSource().setPath("command2")
    command2.getOptions().enable("c2")
    print command1, command2
    
    source = Path("~/deleteme/source/")
    dest = Path("~/deleteme/dest/")
    flags = Option()
    flags.enable("a")
    flags.enable("v")
    flags.enable("u")
    flags.enable("n")
    flags.enable("h")
    flags.enable("exclude", "notyou")
    
    command = Command(source, dest, flags)
    
    profile = Profile("work")
    profile.add(command)
        
    for cmd in profile:
        print cmd.getDescription()
        print str(cmd)
    
#    profile.execute()
#    profile.execute(True)
    