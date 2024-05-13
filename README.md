<h1>Battery Level</h1>
<h2>Description</h2>
Create sensor for each component that contains battery_level in the attributes (As long as the attribute's value is numeric)

<h2>Example</h2>
<pre>
configuration: 
    battery_level:
</pre>

<h2>Custom_updater</h2>
<pre>
custom_updater:
  track:
    - components
  component_urls:
    - https://raw.githubusercontent.com/ngfblog/ha-battery-level/master/battery_level.json
</pre>

