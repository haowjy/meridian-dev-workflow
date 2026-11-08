# Cinematic Scroll

A cinematic scroll page plays like a short film that the visitor's scroll
drives: scenes pin in place, progress through, and hand over to the next.
It suits a page with a story or a transformation to show: a product taking
shape, a world, a before and after. It makes a page longer and slower to
skim, so a page whose visitors come to compare plans or find a link is
better served by a normal page with one strong moment. Plan the story with
`resources/motion/directing.md`; this file covers the techniques and how to
build them.

## The Toolbox

Pick each technique for what it does for the story: explain, orient,
reward, connect a cause to its effect, or set the pace. One that does none
of these is noise.

- **Pinned scene.** The stage stays put while the scroll moves things
  within it. Use it when one view deserves sustained attention.
- **Scrubbed sequence.** Values tied directly to scroll progress, so the
  visitor controls the speed and can reverse it: a camera move, an object
  assembling, a path drawing itself.
- **Layered depth.** Foreground, middle and background move at different
  rates. Keep the ratios consistent across the page, or the world seems to
  change size.
- **Masked text reveals.** Lines or words rising through a mask, or text
  filling in as the scroll passes. Keep them for headlines and short lines;
  body text appears whole.
- **Wipes.** `clip-path` or mask transitions between scenes: an iris, a
  wipe, a burn. One transition that recurs becomes the page's signature.
- **Object constancy.** One element carried from scene to scene (a product,
  a character, a card) so the visitor follows it instead of reorienting at
  every cut.
- **Sticky stack.** Cards that pin, scale back and are covered by the next.
- **Horizontal track.** A sticky stage whose content moves sideways while
  the visitor scrolls down. Good for a timeline or a gallery.
- **Image-sequence or video scrub.** Prerendered frames drawn to a canvas
  by scroll position, for 3D or footage too heavy to render live.
- **Shader scenes.** A WebGL sky, fire, fluid or noise field behind the DOM,
  driven by the same progress values as everything else.
- **Environment shift.** Light, colour or weather changing across the page
  to mark time passing or a turn in the story.

## Build It on One Timeline

- **Model the page as named scenes on one timeline,** each with a scroll
  range and a local progress from 0 to 1. Every layer reads its state from
  those progress values, never from its own offsets. A moment that several
  layers must agree on (when the creature lands, when the lights go out) is
  a named cue on the timeline, not a number repeated in each layer.
- **A pause is a scene.** To hold a moment longer, give it its own range on
  the timeline rather than stretching the curves inside another scene.
- **Let the page work without the film.** Render the content as ordinary
  markup that reads top to bottom, then let the film take it over. Text that
  matters is readable at rest, never only in the middle of an animation.
- **Keep layout in CSS.** Let CSS place things and have script read the
  result back, so the first paint and the film agree. Script draws per-frame
  values: transforms, opacity, canvas.
- **Separate the world from the stage.** Scenery that persists across scenes
  (sky, mountains, ground) lives on a fixed layer behind the stage, so it
  stays when the stage scrolls away.
- **Scrubbed values use linear or near-linear easing,** with light
  smoothing, so motion tracks the scroll. Easing curves belong inside a
  scene's own moves.
- **Every path through the page works:** scrolling forward and back, fast,
  jumping to an anchor, reloading halfway, resizing, returning to a
  background tab. A scrubbed scene reverses cleanly by construction; a
  time-based one decides on purpose whether it replays.
- **Leave scrolling native.** A smooth-scroll library changes how scroll
  feels on every device and can break anchors, find-in-page and momentum on
  touch. Add one only when the page needs it, and test on a phone.

## Phones

- Recompose each scene for a narrow screen; don't shrink the desktop one.
- On iOS Safari, `100dvh` updates only after a scroll ends, so a stage
  sized with it jumps. Size the stage with `100lvh` (the screen with the
  address bar collapsed), lay out what must stay visible in the `100svh`
  area at its top, and let scenery run into the strip between the two.
  Only a real iPhone shows whether this works; desktop Chromium has no
  collapsing address bar.
- A glow or scene element wider than the screen makes iOS Safari zoom the
  whole page out, and `overflow-x: clip` on `body` doesn't prevent it. Clip
  on the element's own section.

## Performance and Access

- Run one animation loop for the whole film, skip painting when nothing
  changed, and pause canvases and shaders that are off screen or in a hidden
  tab.
- Measure frame times on a mid-range phone, not only a desktop. Let shaders
  lower their resolution when frames run slow.
- Under `prefers-reduced-motion`, show each scene's resting state with the
  full story and content, and change between scenes with a crossfade or
  instantly. Nothing flashes more than three times a second.
