# astronomical-distance
Fast and easy distance calculation based on observed stellar parallax in parsecs and lightyears. Writes output to json that you can view afterwards or parse if needed.

I tried doing this properly but failed because I'm dumb so instead of being a nice learning experience it sucks and is oversimplified but accurate.

General formula for star distance calculation should be Ds = AU / tan (theta / 3600), where theta is angle of observed parallax in arcseconds, however it did not work to my surprise and unamusement so I just went for something easier.
