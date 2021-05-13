'''

To declare an encoding other than the default one, a special comment line should be added as the first line of the file. The syntax is as follows:

# -*- coding: encoding -*-
where encoding is one of the valid codecs supported by Python.

For example, to declare that Windows-1252 encoding is to be used, the first line of your source code file should be:

# -*- coding: cp1252 -*-
One exception to the first line rule is when the source code starts with a UNIX “shebang” line. In this case, the encoding declaration should be added as the second line of the file. For example:

#!/usr/bin/env python3
# -*- coding: cp1252 -*-


'''

# -*- coding: encoding -*-

# -*- coding: cp1252 -*-

#!/usr/bin/env python3
# -*- coding: cp1252 -*-