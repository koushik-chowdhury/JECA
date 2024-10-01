# Kernel and Shell

## 1. Kernel:
- The kernel is the **core part of an operating system**.
- It manages the system's resources and acts as a bridge between hardware and software.
- It directly interacts with the hardware, like CPU, memory, and devices (e.g., disk drives), and handles tasks such as:
  - Process management (creating, scheduling, and terminating processes).
  - Memory management (allocating and freeing up memory).
  - Device management (communicating with peripheral devices).
  - File system management (reading/writing files).
- The kernel operates in **privileged mode**, meaning it has complete access to all resources on the computer.

> [!NOTE]  
> Developed in 1969 by AT & T's employees

### Types of Kernels:
- **Monolithic kernel** (e.g., Linux kernel): All system services run in kernel space.
- **Microkernel** (e.g., MINIX): Only essential services run in kernel space; other services run in user space.

---

## 2. Shell:
- The shell is the **interface** that allows users to interact with the operating system.
- It acts as a middleman between the user and the kernel, interpreting and executing user commands.
- The shell provides a way to run programs, manage files, and perform other tasks via a **command-line interface (CLI)** or a **graphical user interface (GUI)**.

### Popular Shells in UNIX-like Systems:
- **Bash** (Bourne Again Shell).
- **Zsh** (Z shell).
- **Fish** (Friendly Interactive Shell).

---

### In summary:
- **Kernel**: Manages hardware and system resources.
- **Shell**: Provides the user interface to interact with the operating system.
---

# `ls` Command in Linux

The `ls` command is used to **list directory contents** in Linux and other Unix-like operating systems. It provides information about files and directories within the current or specified directory.

## Basic Syntax:
```bash
ls [OPTION]

```
| Option           | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `-a`             | **Show all files**, including hidden files (those starting with a dot `.`).  |
| `-l`             | **Long listing format** showing detailed information (permissions, size, etc.). |
| `-h`             | **Human-readable sizes** (e.g., KB, MB) when used with `-l`.                |
| `-R`             | **Recursively list** all files in subdirectories.                           |
| `-t`             | Sort files by **modification time**, with the most recent first.            |
| `-S`             | Sort files by **file size**, with the largest files first.                  |
---

# `whoami` Command in Linux

The `whoami` command in Linux and Unix-like systems is used to display the **username** of the current user.

## Details:
- It simply returns the effective username of the user who is currently logged into the system or executing the command.
- Commonly used to verify which user account is in use, especially when switching between user accounts.

## Basic Syntax:
```bash
whoami
```
---

# System Shutdown and Reboot Commands in Linux

Linux provides several commands for shutting down, rebooting, or halting the system. Each of these commands can be used for different purposes and situations.

## 1. `halt`
- **Description**: The `halt` command is used to stop the system.
- **Functionality**: It stops all processes but does not necessarily power off the machine.
- **Syntax**:
  ```bash
  halt
  ```
## 2. `init 0`
- **Description**: The `init` command controls the system runlevels. `init 0` is used to **shut down** the system (go to runlevel 0).
- **Functionality**: It performs an orderly shutdown and powers off the system.
- **Syntax**:
  ```bash
  init 0
  ```
  ## 3. `init 6`
- **Description**: The `init` command controls the system runlevels. `init 6` is used to **reboot** the system by switching to runlevel 6.
- **Functionality**: It gracefully reboots the system.
- **Syntax**:
  ```bash
  init 6
  ```
## 4. `poweroff`
- **Description**: The `poweroff` command is used to power down the system.
- **Functionality**: It is similar to the `halt` command but will attempt to power off the machine completely.
- **Syntax**:
  ```bash
  poweroff
  ```
## 5. `reboot`
- **Description**: The `reboot` command is used to restart the system.
- **Functionality**: It reboots the system immediately.
- **Syntax**:
  ```bash
  reboot
  ```
  ## 6. `shutdown`
- **Description**: The `shutdown` command schedules a system shutdown. You can specify a delay or shut down immediately.
- **Functionality**: It can also reboot the system.
- **Syntax**:
  ```bash
  shutdown [OPTION] [TIME]
  ```
  - Options
    - `-h`: Halt the system
    - `r`: Reboot the stytem
  - Time
    - `now`: Shutdown/Reboot Immediatly
    - `+5`:

| Command    | Action               | Description                                         |
|------------|----------------------|-----------------------------------------------------|
| `halt`     | Stop system           | Stops the system but doesn't necessarily power it off. |
| `init 0`   | Shutdown              | Initiates shutdown, switches to runlevel 0.         |
| `init 6`   | Reboot                | Reboots the system, switches to runlevel 6.         |
| `poweroff` | Power off             | Powers off the system.                              |
| `reboot`   | Reboot                | Restarts the system.                                |
| `shutdown` | Schedule shutdown     | Shuts down or reboots the system at a specified time. |
