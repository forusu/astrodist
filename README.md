# astronomical-distance
Fast and easy distance calculation based on observed stellar parallax in parsecs and lightyears. Writes output to json that you can view afterwards or parse if needed.

I tried doing this properly but failed because I'm dumb so instead of being a nice learning experience it sucks and is oversimplified but accurate.

General formula for star distance calculation should be Ds = AU / tan (theta / 3600), where theta is angle of observed parallax in arcseconds, however it did not work to my surprise and unamusement so I just went for something easier.

# features
* Calculate astronomical distances in parsecs, lightyears and meters using measured stellar parallax
* Visualise the result with ascii
* Write the output to a file for easy viewing after multiple calculations

![](https://media.discordapp.net/attachments/751326505694658654/813348397984907314/unknown.png)
