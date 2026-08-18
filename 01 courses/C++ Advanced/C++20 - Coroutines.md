# C++20 - Coroutines

# References

[C++20’s Coroutines for Beginners - Andreas Fertig - CppCon 2022](https://youtu.be/8sEe-4tig_A?si=MLQJuYdBHScSgeBu)

[C++ Coroutines, from Scratch - Phil Nash - CppCon 2022](https://youtu.be/EGqz7vmoKco?si=E-GJaLH4hVgPzAdp)

[Deciphering C++ Coroutines - A Diagrammatic Coroutine Cheat Sheet - Andreas Weis - CppCon 2022](https://youtu.be/J7fYddslH0Q?si=fBxfaCgi32koLRc5)

[CppCon 2016: James McNellis “Introduction to C++ Coroutines"](https://youtu.be/ZTqHjjm86Bw?si=z9DgFBD0USNDdATq)

[Daily bit(e) of C++ | Coroutines: step by step](https://simontoth.substack.com/p/daily-bite-of-c-coroutines-step-by)

[https://github.com/StudioAlbert/C__Course_Coroutines](https://github.com/StudioAlbert/C__Course_Coroutines)

---

## C++ Coroutines: Wide Overview

![source : **C++20’s Coroutines for Beginners - Andreas Fertig - CppCon 2022 ([link](image.png)

source : **C++20’s Coroutines for Beginners - Andreas Fertig - CppCon 2022 ([link](https://youtu.be/8sEe-4tig_A?si=VJGXa43KI_q8k2yN))**

### Specific operators

**co_yield** and **co_await** pauses the coroutine

**co_return** ends the coroutine

![source : **C++20’s Coroutines for Beginners - Andreas Fertig - CppCon 2022 ([link](image%201.png)

source : **C++20’s Coroutines for Beginners - Andreas Fertig - CppCon 2022 ([link](https://youtu.be/8sEe-4tig_A?si=VJGXa43KI_q8k2yN))**

Elements

Wrapper type named promise type, it returned by the coroutine and can control the coroutine.

Awaitable type, use by the co_await instruction

# Simple coroutine

## How to declare  a coroutine

---