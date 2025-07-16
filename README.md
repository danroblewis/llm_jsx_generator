


input

"Presentation Roles"
- list
- table
- heading
- card





LCARS parts, as described by this "LCARS Guideline"
-- http://www.lcars-terminal.de/tutorial/guideline.htm
-- http://www.lcars-terminal.de/tutorial/manifesto.htm
- LCARS Frame
    - like a border, but it doesnt go all the way around
    - has menu items
    - might display a header
- LCARS Swept
    - part of the Frame
- LCARS Cap
    - when rendering a pillbox, either the right or left side has a notch cut out of it
    - these are like a 'period' in grammar

Design stuff
- Spacing
    - there are 2 main spacing constants
- Font
    - there are 3 different sizes of the font
    - main title size, sub-header size, normal data size
- Colors
    - monochrome is fine
    - 2-3 colors is okay
    - 4 colors is a lot
    - 5 colors is maybe too much
    - dont use 6 colors
- Animations
    - avoid obvious repetition
    - avoid syncing animation cycles
- "The LCARS Ratio"
    - text must fit within the ratio
- Swept Frames
    - a swept transitions from horizontal to vertical
    - the two bars should have different thicknesses
    - if a swept connects to another swept, the thicknesses that meet should have  different thickness





this is all working pretty well
i should make a new react hook
```js
function MyComponent(props) {
    const [ Template ] = useLLMJSX("some guidance", [props])

    return <Template {...props} />
}


```



this went pretty well.
the LLMTemplate component works.
i can make components with it now like:
```js
function PersonCard() {
    const somebody = {
        name: "John Doe",
        age: 30,
        city: "New York",
        email: "john.doe@example.com"
    }
    return <LLMTemplate {...somebody} />
}
```
what next?
- pass in pre-existing styles, design principles, or use tailwind
- pass in a list of callback functions for it to use in its template
- pass a description of the type of component it's rendering (card, list, )
- 


