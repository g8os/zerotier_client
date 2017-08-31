FORMAT: 1A
HOST: https://my.zerotier.com/

# ZeroTier Central API

ZeroTier Central's API is (mostly) RESTful and accepts GET and POST requests. PUT is treated as a synonym of POST. All posted payloads must be JSON (content type header is ignored). Field types are generally strict, e.g. a field that takes an integer may ignore or return an error if set to a string or a boolean. Writes to unrecognized or read-only fields are ignored. Unless you are running a private instance of Central configured to accept plain *http*, all requests must be *https*.

Token authentication is accomplished by sending the following header: `Authorization: bearer <API token>` API tokens may be created and viewed in your user configuration. Guard your API tokens very carefully.

This documentation is written in [API blueprint](https://apiblueprint.org) format and is [available in raw MSON form here.](/static/central-api.md).
<br><br>



## Group General Queries

## status [/api/status]

 + Attributes (object)
     + online (boolean) - Always true
     + clock (number) - Current server-side system clock (ms since epoch)
     + version (string) - ZeroTier Central version
     + apiVersion (number) - ZeroTier Central API version
     + uptime (number) - This host's uptime in milliseconds
     + user (object) - Current user if authenticated, otherwise null
     + stripePublishableKey (string) - Publishable key for Stripe payment processor or null if not configured
     + paidPlans (object) - Available paid plans (if configured)
     + smsEnabled (boolean) - True if SMS messaging is available
     + clusterNode (string) - Name of current cluster node servicing this request
     + loginMethods (object) - Object containing login methods and whether they are available
     + recaptchaSiteKey (string) - Recaptcha site key or null if not configured
     + return_to (string) - Bounce destination if using Central as third party auth source (used for ZeroTier support login)

### Get Status and Configuration Information [GET]

Obtain information about this server and/or useful to the Central web UI.

 + Response 200 (application/json)
     + Attributes (status)

## self [/api/self]

### Get Currently Authenticated User [GET]

Get the currently authenticated user's user record.

 + Response 200 (application/json)
     + Attributes (User)

## randomToken [/api/randomToken]

 + Attributes (object)
     + token (string) - Random string suitable for use as an API authentication token
     + clock (number) - Current server-side system clock (ms since epoch)
     + raw (string) - Raw random bytes in hex format

### Generate a Random Token [GET]

This generates a random token suitable for use as an API token server-side using a secure random source. It does not actually modify the user record, just returns the token for use by API callers or the UI.

 + Response 200 (application/json)
     + Attributes (randomToken)

## logout [/api/auth/_logout]

### Terminate Current Session [POST]

Hitting this endpoint causes the user to be logged out. It has no effect when using token authentication, so it's mostly used by the UI.

 + Response 200 (application/json)




## Group User

## User [/api/user/{userId}]

 + Parameters
     + userId: 00000000-0000-0000-0000-000000000000 (required,string) - Internal user ID (GUID)

 + Attributes (object)
 
     + id (string) - User ID (GUID) [ro]
     + type (string) - Object type [ro]
     + clock (number) - Current system clock on server [ro]
     + globalPermissions (object) - Global permissions for this user against all objects on system (for admins) [ro]
         + r (boolean) - Read
         + m (boolean) - Modify
         + d boolean) - Delete
         + a (boolean) - Authorize
     + ui (object) - Arbitrary data that is stored and used by the UI [rw]
     + displayName (string) - User display name [rw]
     + email (string) - User e-mail [ro]
     + auth (object) - Object containing one or more authentication types and login names or IDs [ro]
     + smsNumber (string) - SMS telephone number for sending SMS notifications [rw]
     + tokens (array[string]) - Array of API authentication tokens [rw]
     + permissions (object) - Actors with permissions that apply to this object [ro]
         + {id} (object) - Permissions possessed by actor object, by object ID [ro]
              + t (string) - Type of actor object (currently User or Group)
              + r (boolean) - Read
              + m (boolean) - Modify
              + d (boolean) - Delete
              + a (boolean) - Authorize
     + subscriptions (object) - Subscriptions by plan ID [ro]

### Retrieve a User [GET]

 + Response 200 (application/json)
     + Attributes (User)

### Update a User [POST]

Only fields marked as [rw] can be directly modified. If other fields are present in the posted request they are ignored.

 + Request (application/json)

 + Response 200 (application/json)
     + Attributes (User)

## Users [/api/user]

 + Attributes (array[User])

### Get All Viewable Users [GET]

Get all users for which you have at least read access.

 + Response 200 (application/json)
     + Attributes (Users)




## Group Network

## Network [/api/network/{networkId}]

 + Parameters
     + networkId: 0000000000000000 (required,string) - 16-digit ZeroTier network ID

 + Attributes (object)
     + id (string) - 16-digit ZeroTier network ID [ro]
     + type (string) - Object type ("Network") [ro]
     + clock (number) - Current system clock on server [ro]
     + ui (object) - Arbitrary data that is stored and used by the UI [rw]
     + rulesSource (string) - Source code of network rule set [rw]
     + description (string) - Long description of this network [rw]
     + permissions (object) - Actors with permissions that apply to this object [ro]
         + {id} (object) - Permissions possessed by actor object, by object ID [ro]
              + t (string) - Type of actor object (currently User or Group)
              + r (boolean) - Read
              + m (boolean) - Modify
              + d (boolean) - Delete
              + a (boolean) - Authorize
     + onlineMemberCount (number) - Number of members online [ro]
     + capabilitiesByName (object) - Capabilities defined in rule set by name [rw]
     + tagsByName (object) - Tags defined in rule set by name [rw]
     + circuitTestEvery (number) - Circuit test this network every N milliseconds [ro]
     + config (ControllerNetworkConfig) - Network configuration (for actual controller) [rw]

### Retrieve a Network [GET]

 + Response 200 (application/json)
     + Attributes (Network)

### Update or create a Network [POST]

Only fields marked as [rw] can be directly modified. If other fields are present in the posted request they are ignored.

New networks can be created by POSTing to `/api/network` with no networkId parameter. The server will create a random unused network ID and return the new network record.

 + Request (application/json)
     + Attributes (Network)

 + Response 200 (application/json)
     + Attributes (Network)

### Delete a Network [DELETE]

Delete a network and all its related information permanently. Use extreme caution as this cannot be undone!

 + Response 200

## Networks [/api/network]

 + Attributes (array[Network])

### Get All Viewable Networks [GET]

Get all networks for which you have at least read access.

 + Response 200 (application/json)
     + Attributes (Networks)




## Group Member

## Member [/api/network/{networkId}/member/{nodeId}]

 + Parameters
     + networkId: 0000000000000000 (required,string) - 16-digit ZeroTier network ID
     + nodeId: 0000000000 (required,string) - 10-digit ZeroTier node ID (a.k.a. ZeroTier address)

 + Attributes (object)
     + id (string) - Member record ID, which is formed from the network and node IDs [ro]
     + type (string) - Object type ("Member") [ro]
     + clock (number) - System clock on server [ro]
     + networkId (string) - 16-digit ZeroTier network ID [ro]
     + nodeId (string) - 10-digit ZeroTier node ID / device address [ro]
     + controllerId (string) - 10-digit ZeroTier node ID of controller (same as first 10 digits of network ID) [ro]
     + hidden (boolean) - Hidden in UI? [rw]
     + name (string) - Short name describing member [rw]
     + description (string) - Long form description [rw]
     + online (boolean) - Member is online? (has requested an update recently) [ro]
     + lastOnline (number) - Time member was last determined to be online [ro]
     + lastOffline (number) - Time member was last determined to be offline [ro]
     + physicalAddress (string) - Latest physical address of member [ro]
     + physicalLocation (array) - Lat/lon of estimated (GeoIP-determined) location of physicalAddress (if available) [ro]
     + clientVersion (string) - Most recent client software version [ro]
     + protocolVersion (number) - Most recent client-reported ZeroTier protocol version [ro]
     + supportsCircuitTesting (boolean) - True if member supports circuit testing [ro]
     + supportsRulesEngine (boolean) - True if member supports the new (post-1.2) rules engine [ro]
     + offlineNotifyDelay (number) - Notify of offline after this many milliseconds [rw]
     + config (ControllerMemberConfig) - Member configuration (for actual controller) [rw]

### Retrieve a Member [GET]

 + Response 200 (application/json)
     + Attributes (Member)

### Update or add a Member [POST]

New members can be added to a network by POSTing them.

 + Request (application/json)
     + Attributes (Member)

 + Response 200 (application/json)
     + Attributes (Member)

## Data Structures

### ControllerNetworkConfig
 + id (string) - 16-digit ZeroTier network ID [ro]
 + nwid (string) - 16-digit ZeroTier network ID (for backward compatibility) [ro]
 + name (string) - Short name of network [rw]
 + objtype (string) - Object type on controller ("network") [ro]
 + private (boolean) - If true, certificate access control is enabled [rw]
 + creationTime (number) - Time network was created on controller [ro]
 + revision (number) - Network revision number [ro]
 + lastModified (number) - Time config was last modified [ro]
 + multicastLimit (number) - Max recipients per multicast or broadcast [rw]
 + routes (array[object]) - Array of IP routes published to members [rw]
 + rules (array[object]) - Network base rules table [rw]
 + tags (array[object]) - Array of tags available on this network [rw]
 + capabilities (array[object]) - Array of capabilities available on this network [rw]
 + totalMemberCount (number) - Total number of members [ro]
 + activeMemberCount (number) - Number of active/online members [ro]
 + authTokens (array[string]) - Array of authentication tokens for auto-authorizing new members [rw]
 + authorizedMemberCount (number) - Number of authorized members [ro]
 + v4AssignMode (object) - Boolean toggles for IPv4 assignment modes [rw]
 + v6AssignMode (object) - Boolean toggles for IPv6 assignment modes [rw]

### ControllerMemberConfig
 + id (string) - 10-digit ZeroTier node ID [ro]
 + address (string) - 10-digit ZeroTier node ID [ro]
 + nwid (string) - 16-digit network ID [ro]
 + objtype (string) - Object type on controller ("member") [ro]
 + authorized (boolean) - True if authorized (only matters on private networks) [rw]
 + authHistory (array[object]) - History of most recent authentications [ro]
 + capabilities (array[number]) - Array of IDs of capabilities assigned to this member [rw]
 + tags (array[array[number]]) - Array of tuples of tag ID, tag value [rw]
 + creationTime (number) - Time member record was first created [ro]
 + identity (string) - ZeroTier public identity of member (address and public key) [ro]
 + ipAssignments (array[string]) - Array of IP assignments published to member [rw]
 + lastAuthorizedTime (number) - Time member was last authorized on network [ro]
 + lastDeauthorizedTime (number) - Time member was last de-authorized on network [ro]
 + noAutoAssignIps (boolean) - If true do not auto-assign IPv4 or IPv6 addresses, overriding network settings [rw]
 + physicalAddr (string) - Last known physical address of member [ro]
 + revision (number) - Member record revision counter [ro]