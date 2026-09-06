---
title: Particle Systems
type: course
status: Backlog
subject: Unity
bloc: "[[VFX, Rendu et Game Feel]]"
created: 2022-12-13T23:04
---
# Particle Systems

### Different render pipelines

In Unity, there are four main render pipelines: the Built-in Render Pipeline (BRP), the Universal Render Pipeline (URP), the High Definition Render Pipeline (HDRP), and the Scriptable Render Pipeline (SRP). Here are the differences between these four pipelines:

1. Built-in Render Pipeline (BRP): The BRP is the original render pipeline in Unity. It is a fixed-function pipeline, meaning that its rendering stages are fixed and cannot be modified. It supports a wide range of rendering features, including advanced lighting, shadowing, and post-processing effects, but it can result in lower performance on lower-end devices.
2. Universal Render Pipeline (URP): The URP is a lightweight, data-driven pipeline designed for mobile, VR, and AR platforms. It is optimized for performance and supports features that are designed to work well on a wider range of devices. It is highly customizable and provides a simplified workflow that is easier to work with than the BRP.
3. High Definition Render Pipeline (HDRP): The HDRP is a high-end pipeline designed for high-quality graphics and photorealistic rendering. It supports advanced features such as real-time ray tracing, physically-based rendering, and dynamic lighting. It is best suited for large and complex projects that require high-quality graphics.
4. Scriptable Render Pipeline (SRP): The SRP is a flexible and customizable pipeline that allows developers to create their own rendering pipelines using C# scripts. It provides a high degree of control over the rendering process and allows for the creation of pipelines that are optimized for specific platforms or projects.

In summary, the BRP is best suited for large and complex projects that require high-quality graphics and advanced features. The URP is designed for mobile, VR, and AR platforms and is optimized for performance and compatibility with a wide range of devices. The HDRP is a high-end pipeline designed for high-quality graphics and photorealistic rendering, while the SRP is a flexible and customizable pipeline that allows for the creation of custom pipelines using C# scripts.
