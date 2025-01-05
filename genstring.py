import asyncio
from pyrogram import Client

API_ID = input("\nMasukkan API_ID Anda:\n > ")
API_HASH = input("\nMasukkan API_HASH Anda:\n > ")

# Gantilah dengan nama bot Anda atau string unik
NAMA_SESI = "ranzstring"

async def main():
    # Inisialisasi Client dengan nama sesi, API ID, dan API Hash
    async with Client(NAMA_SESI, api_id=API_ID, api_hash=API_HASH) as client:
        # Ekspor string sesi
        ss = await client.export_session_string()
        print("\nINI ADALAH STRING SESI ANDA, SALIN DAN JANGAN BAGIKAN!!\n")
        print(f"\n{ss}\n")
        print("\nSTRING TELAH DIBUAT\n")
        
        # Siapkan pesan
        xx = f"INI ADALAH STRING SESI ANDA, SALIN DAN JANGAN BAGIKAN!!\n\n`{ss}`\n\nSTRING TELAH DIBUAT"
        
        try:
            # Kirim string sesi ke diri Anda sendiri
            await client.send_message("me", xx)
        except Exception as e:
            print(f"Gagal mengirim pesan: {e}")

# Jalankan fungsi utama
asyncio.run(main())