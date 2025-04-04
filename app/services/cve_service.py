import httpx

BASE_URL = "https://cve.circl.lu/api/cve/"

async def fetch_cve(cve_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL + cve_id)
        if response.status_code == 200:
            return response.json()
        return {"error": f"{cve_id} not found"}
