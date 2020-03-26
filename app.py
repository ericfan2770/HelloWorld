# Package: like a folder, a folder for modules

import ecommerce.shipping
ecommerce.shipping.calc_shipping()  # can often be verbose

# import individual methods/functions
from ecommerce.shipping import calc_shipping, calc_tax
calc_shipping()

# import entire module
from ecommerce import shipping
shipping.calc_shipping()

# from usage:
# from <package> import <module> OR
# from <package.module> import <function/method>

