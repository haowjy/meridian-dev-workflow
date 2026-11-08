# Directing Motion That Tells a Story

A scroll film, an animated explainer, or a hero scene where characters and
objects act is judged as a sequence: does the viewer understand what
happened, and why? Good individual frames don't add up to that by
themselves. Most failures in these pieces are failures between frames: an
effect with no visible cause, a character facing the wrong way, scenery that
vanishes, a moment the viewer's eye never reaches. Direct the piece the way
an animation director would, before and after you build it.

## Write the Beats First

Before building, write the sequence as beats, one line each, and show it to
whoever owns the story or the visual direction. A beat sheet is cheap to
change; a built scene isn't. For each beat, write:

- **What the viewer understands by its end.** One thing. A beat that has to
  land two things is two beats.
- **What causes it.** When the cause happens on screen, show it before
  its effect: if the dragon's breath freezes the sky, show the breath, then
  the sky changing. An outcome with no visible cause reads as arbitrary,
  so when the cause stays off screen, let the viewer infer it from what
  they do see.
- **Who acts.** Every character the story names gets an action the viewer
  can read: their own attack, gesture, or reaction, not a place in a crowd.
- **Where things move,** and which way they face.
- **What carries into the next beat:** who is still there, where they
  stand, what is still burning or glowing.

Build in beat order and keep timing in one place, a timeline of named beats
with their ranges, so a beat can be lengthened or moved without hunting
through code.

## Stage Each Moment

- **One focal action at a time.** Put the action the beat is about where the
  eye already is, give it the most contrast and the most motion, and keep
  everything else quieter. When two things compete, one of them waits.
- **Lead the eye with light.** The brightest, highest-contrast area is where
  people look. A darkening layer added so text stays readable goes away when
  the text does; otherwise it dims the action that follows.
- **Balance the frame for the action, not the layout.** Visual weight piles
  up where detail, contrast and motion gather. A side crowded with mountains
  and aurora pulls the eye away from a character on the other side.
- **Scale and pose carry meaning.** Decide what each figure's size and
  pose should say (power, weight, rest, fear) and check that they say it:
  a creature at rest on the ground stops the flapping it used to fly; a
  body thrown across the frame lands somewhere you can see.
- **Show the reaction.** An action reads through what it does to the
  surroundings: the party gives ground, the sky flares, the hit flinches.
  An effect that the story says persists keeps going for as long as it
  matters, not for one pulse.
- **Recompose for a phone; don't just crop.** Check each beat at phone width
  for action pushed off the edges, and pull the staging in.

## Keep Continuity

Continuity is what lets the viewer trust the world. Check every beat
against these:

- **Things persist within a continuous scene.** Whatever exists stays, in
  the same place, until something in the scene removes it. Scenery belongs
  to the world, not to a character or a scene's layer, so it doesn't leave
  when they do. A change of place or time is a deliberate cut, and reads as
  one: a wipe, a fade to black, a new establishing view.
- **Facing follows travel.** A creature faces the direction it moves, except
  where the story turns it on purpose (a face-off, a backward retreat).
- **Direction of travel holds.** A journey that goes left to right keeps
  going left to right. Reverse it only to say something: a retreat, a
  return, a turn.
- **Only the moving things move.** Background drift follows the camera or
  the walkers it belongs to, and stops when they stop. A campfire doesn't
  travel with the people standing up from it.
- **Repeated effects behave the same way** every time they appear. One that
  shows up in some beats and not others reads as a mistake. Make it
  consistent, or cut it.
- **The story's own facts hold.** Weapons, powers and places match the
  written story; check with whoever owns it before inventing one.

When something breaks continuity, find why it happens and fix that. Fading
over a disappearing element, or darkening a muddy area, hides the defect
from the viewer for one beat and moves it to the next.

## Review the Motion, Not the Frames

Stills at a few points show composition; they can't show which way
something travels, whether an attack connects, or whether the trees stay
put. Review each beat as a sequence, in whatever drives it: scroll position
for a scroll film, time for an autoplaying or click-started animation.

1. Capture the beat densely: at least twelve evenly spaced frames across a
   beat with action in it, plus frames at its key moments (an impact, a
   landing, a cut). For a scroll-driven page open in `/meridian-dev-workflow:agent-browser`, this
   skill's `scripts/motion-strip.sh` captures a scroll range as a tiled
   strip and can record a video of it. For a time-based animation, record a
   video and pull frames from it, or pause it at evenly spaced times.
2. Narrate the frames as a stranger would, in order, from the pictures
   alone: who is there, what each does, what happens because of it. Compare
   the narration with the beat sheet. Each place where they differ is a
   defect, or a beat the sheet got wrong. A reviewer who hasn't seen the
   beat sheet gives the most honest narration.
3. Check effects that run on time, such as a pulse, a flicker, or a swell,
   from frames a fraction of a second apart at one position: frames settled
   at each scroll position miss them.
4. For a scroll film, also scroll backward through the range and jump into
   the middle of it: it plays in every direction and from every starting
   point.

Report to the person in scene terms, with the frames: "the dragon lands on
the shore and breathes upward; the party backs away", not the names of
variables, beats or internal labels they never saw. Give them the video for
what frames can't show, such as the size of a pulse or the speed of a
swell, and ask them to watch it.
