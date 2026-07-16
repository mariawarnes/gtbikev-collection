# GTBike V Collection
A collection of mods and tutorials to enhance your GTBike V experience.

> GTBike V is a mod for GTA V by Nestor Matas, (AKA Makinolo). **This collection is not affiliated with Makinolo or Rockstar**.

## Install GTBike V

> This guide starts with a Windows PC that has **only Steam installed**. 

> **Do not use these mods in GTA Online.** ScriptHook and ASI mods are for single-player Story Mode only.

### Step 0 — Choose your starting point

#### GTA V is not installed

1. Open Steam and sign in.
2. Open the **Store** and search for [Grand Theft Auto V Enhanced](https://store.steampowered.com/app/3240220/Grand_Theft_Auto_V_Legacy/).
3. If you do not own GTA V, click **Add to Cart** and complete the purchase. Although the shop product is called Enhanced, the purchase includes both **Grand Theft Auto V Enhanced** and **Grand Theft Auto V Legacy**.
4. Open **Library** and select **Grand Theft Auto V Legacy**. Legacy is a separate library entry and is the recommended edition for GTBikeV.
5. If Legacy does not appear immediately, restart Steam, search the library again, and make sure hidden games are visible.
6. Click **Install**, select an installation drive, and wait for the Legacy download to finish.
7. Click **Play** once to allow Steam to install Rockstar Games Launcher and the other first-run components.
8. Sign in to or create a Rockstar Games account when prompted, and link it to Steam if requested.
9. Once Rockstar Games Launcher setup finishes, close GTA V and the launcher.
10. Continue to Step 1.

#### GTA V is already installed

1. Open Steam and select **Library**.
2. Search for `Grand Theft Auto V`.
3. If **Grand Theft Auto V Legacy** is already installed, select it and continue to Step 1.
4. If only **Grand Theft Auto V Enhanced** is installed, find the separate **Grand Theft Auto V Legacy** entry and click **Install**. Owning the current Steam package includes both editions.
5. If Legacy is owned but does not appear, restart Steam, check hidden games, and search the library again.
6. Wait for the Legacy installation to finish, then continue to Step 1.

### Step 1 — Find the GTA V folder

1. Open Steam Library.
2. Right-click **Grand Theft Auto V Legacy**.
3. Select **Manage → Browse local files**.
4. Keep the folder containing `GTA5.exe` open. This is the **game root**.

The tested location was:

```text
C:\SteamLibrary\steamapps\common\Grand Theft Auto V
```

### Step 2 — Downgrade GTA V Legacy to the compatible executable

The working setup used GTA V Legacy executable version `1.0.3889.0`. Steam's current download may install a newer executable, so download the compatible executable depot before adding the mods.

### Step 3 — Reduce automatic updates

1. In Steam Library, right-click **Grand Theft Auto V Legacy** and select **Properties**.
2. Select **Updates**.
3. Under **Automatic Updates**, choose **Wait until I launch the game**.
4. Scroll to the bottom of the Updates page and find **Build ID**.
5. If the Build ID is `24129523`, the currently installed Steam build needs the downgrade below for this setup.
6. Close the Properties window.

> This does **not** permanently lock the game version: Steam may still require an update when you launch the game.

> Keep the downloaded depot folder so you can copy the compatible files back after any update.

> Do not use **Verify Integrity of Game Files** unless troubleshooting, because verification restores Steam's current files.

> **Build ID note:** Manually copying the older depot files does not change the Build ID displayed by Steam. Steam may continue to show `24129523` afterward even though `GTA5.exe` has been replaced with the compatible `1.0.3889.0` executable.

### Step 4 — Download and apply the compatible depot

1. Close GTA V and Rockstar Games Launcher.
2. Press **Windows key + R**.
3. Enter the following and press Enter:

   ```text
   steam://open/console
   ```

4. Steam will open a **Console** tab.
5. Paste this exact command into the Steam Console and press Enter:

   ```text
   download_depot 271590 271591 6768057890420400504
   ```

   - `271590` is the GTA V Legacy app ID.
   - `271591` is the Legacy executable depot.
   - `6768057890420400504` is the manifest used by the working `1.0.3889.0` setup.

6. Wait until Steam reports that the depot download is complete. It may look inactive while downloading; do not close Steam.
7. Steam normally places the files here:

   ```text
   C:\Program Files (x86)\Steam\steamapps\content\app_271590\depot_271591
   ```

   If Steam is installed elsewhere, use the equivalent `steamapps\content\app_271590\depot_271591` folder inside the Steam installation.

8. Open the downloaded `depot_271591` folder.
9. Select all files and folders inside it and copy them into the GTA V Legacy game root from Step 1.
10. When Windows asks, choose **Replace the files in the destination**.
11. Keep the downloaded depot folder as a backup. A future Steam update or **Verify Integrity of Game Files** can restore the newest executable, in which case repeat Steps 8–10.

> This downloads and replaces the Legacy executable depot only; it is not a full second copy of GTA V.

### Step 5 — Confirm there are no old mods

Check the game root and make sure none are present:

   ```text
   NativeTrainer.asi
   OpenIV.asi
   xinput1_4.dll
   Scripts\NativeUI.dll
   mods\
   ```

If you find any, move them to a backup folder outside GTA V. Do not delete them.

### Step 6 — Install the Windows prerequisites

1. Download and install [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48).
2. Restart Windows if the installer requests it.
3. Download the latest supported **x64** [Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist).
4. Run its installer and choose **Install**. If it is already present, choose **Repair** or close the installer.
5. Restart Windows if requested.

### Step 7 — Disable BattlEye for Story Mode

1. Open Notepad.
2. Enter this exact line:

   ```text
   -nobattleye -noBE
   ```

3. Save it as `args.txt` in the game root.
4. Open **Rockstar Games Launcher** and sign in.
5. Select **Settings** in the top-right corner.
6. On the launcher Settings page, locate the BattlEye option. Depending on the launcher version, it may appear in **General** or as a checkbox labelled **Enable BattlEye**.
7. Clear the **Enable BattlEye** checkbox so it is unchecked.
8. Close the Settings page. The launcher saves the change automatically.

> The Rockstar setting and `args.txt` serve the same purpose, but using both makes the Story Mode configuration explicit when launching the Steam edition through Rockstar Games Launcher.

> If the checkbox is not shown, leave `args.txt` in the game root and continue. Do not delete the `BattlEye` folder, uninstall its service, or disable security software.

> With BattlEye disabled GTA Online will not connect. To use GTA Online later, first remove or isolate the mod files, remove the `-nobattleye -noBE` arguments, and re-enable **Enable BattlEye** in Rockstar Games Launcher.

### Step 8 — Install GTBikeV and its ScriptHook components

1. Download the **GTBikeV v0.8.0.4 Installer** from the [official downloads page](https://www.gtbikev.com/downloads/).
2. Close GTA V, Steam, and Rockstar Games Launcher.
3. Run the installer.
4. On the component-selection screen, keep **GTBikeV** selected.
5. Also select the combined option that installs **ScriptHookV and ScriptHookVDotNet**. The installer will install both required scripting components.
6. Leave GTBikeV's own files and required libraries selected.
7. When asked for the GTA V location, select the Legacy game root containing `GTA5.exe`.
8. Continue through the installer and allow it to download and install the selected components.
9. Finish and close the installer.

## Step 9 — Launch GTBikeV

1. Start GTA V with BattlEye disabled.
2. Enter Story Mode only.
3. Wait for the scripts to load.
4. Use the GTBikeV interface to select your trainer or sensors.

## Troubleshooting

### No `asiloader.log`

1. Confirm `dinput8.dll` is next to the game executable.
2. Confirm BattlEye is disabled.
3. Confirm `args.txt` contains `-nobattleye -noBE`.
4. Confirm ScriptHookV supports the installed GTA V build.

### ScriptHookVDotNet does not start

1. Confirm `ScriptHookVDotNet.asi` is in the game root.
2. Confirm all SHVDN files came from one release.
3. Install or repair .NET Framework 4.8 and the Visual C++ Redistributable.

### SHVDN starts but GTBikeV does not

1. Confirm `Scripts\GTBikeV.dll` exists.
2. Confirm the complete GTBikeV `Scripts` folder was copied.
3. Confirm `Scripts\mod_textures` exists.
4. Move optional mods out again and retest.

### GTA V was updated

Steam updates and file verification can replace the downgraded executable and mod files. Repeat the depot copy in [Step 4](#Step 4 — Download and apply the compatible depot), then rerun the GTBikeV installer from [Step 8](Step 8 — Install GTBikeV and its ScriptHook components) if its files were replaced.


## Recommended Extra Mods

### [100% Game Save by DireZephyr](https://www.gta5-mods.com/misc/100-save-game)
**Purpose**: Unlocks all the outfit choices for all characters.

> **Warning:** A downloaded save can replace one of your Story Mode save slots. Back up your entire profile folder before copying it.

1. Launch Story Mode at least once so GTA V creates your profile folder, then close the game.
2. Open File Explorer.
3. Go to:

   ```text
   Documents\Rockstar Games\GTA V\Profiles
   ```

   If Windows redirects Documents through OneDrive, use:

   ```text
   OneDrive\Documents\Rockstar Games\GTA V\Profiles
   ```

4. Open the folder with a random-looking profile ID, for example `A1B2C3D4`.
5. Copy that entire profile folder to a safe backup location.
6. Open the downloaded 100% save archive.
7. Copy these two files into your profile-ID folder:

   ```text
   SGTA50015
   SGTA50015.bak
   ```

8. If files with those names already exist, either keep your backup and replace them or rename the downloaded pair to an unused matching save-slot number. Both filenames must use the same number.
9. Launch GTA V and enter Story Mode.
10. If the save does not load automatically, open the pause menu and select **Game → Load Game**, then choose the new save slot.

### [Straight To Story Mode by Chiheb-Bacha](https://www.gta5-mods.com/scripts/straight-to-story-mode)
**Purpose**: Makes getting into the game quicker.

### [Activity Ghosts by oldnapalm](https://github.com/oldnapalm/ActivityGhosts)
**Purpose**: Gives you a physical manifestation of your previous best time to chase to push you for a PB.
