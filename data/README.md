### Copernicus CDS API Key Setup
This 9 step setup guide was based on the open source github from Ørpheus AI. 

> [!IMPORTANT]
> To download ERA5 data via the Climate Data Store (CDS) API, you must provide a Copernicus CDS personal access token (API key). Follow the steps below to create an account, retrieve your key, and accept the dataset license.

1. Go to the official [CDS API setup page](https://cds.climate.copernicus.eu/how-to-api).
2. Click on the **Login / Register** button in the top-right corner of the page.
3. Click **I understand** on the prompt to proceed to the login portal.
4. Unless you already have an ECMWF/Copernicus account, click the **Register** button below the login fields.
5. Fill in your details, (complete the CAPTCHA if its prompted), and click **Register**. Ensure you have access to the email address provided.
6. Open your inbox and click the verification link in the email sent from `servicedesk@ecmwf.int`. If you are not redirected to the profile completion form, return to the link in Step 1 and log in.
7. Fill in the remaining profile details, accept the required agreements, and click **Activate your profile**.
8. You should be redirected back to the [CDS API documentation page](https://cds.climate.copernicus.eu/how-to-api). Scroll down to the section titled **1. Setup the CDS API personal access token**. You will see a code block formatted like this:

   ```yaml
   url: [https://cds.climate.copernicus.eu/api](https://cds.climate.copernicus.eu/api)
   key: YOUR_API_KEY_THAT_SHOULD_BE_COPIED
   ```

   Copy the token string following `key:` and add it to your configuration (for example, in your `.env` file under `CDS_API_KEY` or in your `~/.cdsapirc` file).

9. **Accept the dataset license:** Go to the [ERA5 dataset download page](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download#manage-licences), scroll to the **Terms of use** section, and accept the license. API requests for ERA5 data will be rejected until these terms are accepted on your account.

Once configured, the dataloader will have access to download ERA5 data.