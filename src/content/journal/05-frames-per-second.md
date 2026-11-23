---
title: Frames per Second
order: 5
series: Unity basics
summary: Closing the Catlike Coding basics with the profiler and a home-made FPS counter.
objectives: ../../assets/journal/entry5/objectives.png
video: /videos/journal-entry5.mp4
---

Closing the Basics section of Catlike Coding. The last tutorial covers testing performance, using the Unity profiler and building our own frame rate counter.

Testing, testing, testing.

Now that I have completed this last section, I can work on redesigning my website. The FPS counter is small but it shows HighestFPS, AverageFPS and LowestFPS. It also changes colors depending on certain ranges. Oops, my background music was recorded on my video.

<details>
<summary>Class notes</summary>

- **Why use FixedUpdate and not Update?** Using FixedUpdate keeps the spawning independent of the frame rate. If the configured time between spawns is shorter than the frame time, using Update would cause spawn delays.
- **Why is motion not fluid for low time scales?** Because the fixed time step is constant, the physics system will update less often. Physics objects will remain motionless until a fixed update happens, which is only once every few frames.

  You can counter this by decreasing the fixed time step as you increase the time scale. You can change the interpolation mode of rigidbody components so they interpolate between physics steps, hiding the low update frequency.
- Turn off vsync to have a better idea of how much CPU resources the scene needs.
- You can enforce a maximum frame rate by setting the `Application.targetFrameRate` property. This setting persists in the editor even after exiting play mode. Setting it to -1 will remove the limitation.
- If you want to remove the editor from the performance measurements, you need to make a standalone build with Development Build enabled.
- The profiler does not give a good measurement of frame rate.
- **How does `public int FPS { get; private set; }` work?** Properties are methods that pretend to be a field. We provide the FPS as public information, but only the component itself needs to update the value. The syntax used is shorthand notation for an automatically generated property, which would look something like this:

  ```csharp
  int fps;
  public int FPS {
    get { return fps; }
    private set { fps = value; }
  }
  ```

  This shorthand does not work with Unity's serialization.
- We measure the frames per second each update by dividing 1 by the unscaled time delta of the current frame. The time delta is not the actual time it took to process the last frame, it is influenced by the current time scale. FPS will be wrong unless the time scale is set to 1.
- By using the following approach, we create a new string object with each update, which is discarded next update. This pollutes managed memory which will trigger the garbage collector. This could be troublesome for smaller devices. It also pollutes the profiler data, which makes it harder to find allocations.

  ```csharp
  void Update() { fpsLabel.text = Mathf.Clamp(fpsCounter.FPS, 0, 99).ToString(); }
  ```

  To mitigate this problem we create a fixed array of string representations of every number we might need; this eliminates all temporary string allocations.
- Updating the FPS value each frame will make the label fluctuate constantly when the frame rate isn't stable, making it hard to get a useful reading.

  A solution is to average the frame rate, smoothing the impact of sudden changes. We use a buffer to store the FPS values of multiple frames, plus an index so we know where to put the data of the next frame.

  Initialize the buffer if needed, either because we just started or because frameRange has changed. Then the buffer needs to be updated, after which the average FPS can be calculated. Updating the buffer is done by storing the current FPS at the current index, which is then incremented (`fpsBufferIndex++`).

  We wrap the index around to the start of the array, so we can override the oldest value with the newest once the buffer has been filled.
- By using `[SerializeField]` and `[System.Serializable]` we can expose private variables in the Editor.

</details>
