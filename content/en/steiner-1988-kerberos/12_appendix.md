---
paper: steiner-1988-kerberos
title: 'Kerberos: An Authentication Service for Open Network Systems'
authors:
  - Jennifer G. Steiner
  - Clifford Neuman
  - Jeffrey I. Schiller
year: 1988
venue: USENIX Winter Conference
field: security
section_title: Appendix
kind: appendix
lang: en
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.112.9002
pdf_sha256: 2dd6604c96afde95681d25fe32df9834aad32274d1bdbb44dd5f69d6b9660f59
pdf_pages: 13-14
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 51c6c05110ae5ae41f6b9f505c0bafa5d6b8eb236567f5018b610618b218810e
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Kerberos Application to SUN’s Network File System (NFS)

A key component of the Project Athena workstation system is the interposing of the network between the user’s workstation and her/his private file storage (home directory). All private storage resides on a set of computers (currently VAX 11/750s) that are dedicated to this purpose. This allows us to offer services on publicly available UNIX workstations. When a user logs in to one of these publicly available workstations, rather then validate her/his name and password against a locally resident password file, we use Kerberos to determine her/his authenticity. The login program prompts for a username (as on any UNIX system). This username is used to fetch a Kerberos ticket-granting ticket. The login program uses the password to generate a DES key for decrypting the ticket. If decryption is successful, the user’s home directory is located by consulting the Hesiod naming service and mounted through NFS. The login program then turns control over to the user’s shell, which then can run the traditional per-user customization files because the home directory is now “attached” to the workstation. The Hesiod service is also used to construct an entry in the local password file. (This is for the benefit of programs that look up information in /etc/passwd.)

From several options for delivery of remote file service, we chose SUN’s Network File System. However this system fails to mesh with our needs in a crucial way. NFS assumes that all workstations fall into two categories (as viewed from a file server’s point of view): trusted and untrusted. Untrusted systems cannot access any files at all, trusted can. Trusted systems are completely trusted. It is assumed that a trusted system is managed by friendly management. Specifically, it is possible from a trusted workstation to masquerade as any valid user of the file service system and thus gain access to just about every file on the system. (Only files owned by “root” are exempted.)

In our environment, the management of a workstation (in the traditional sense of UNIX system management) is in the hands of the user currently using it. We make no secret of the root password on our workstations, as we realize that a truly unfriendly user can break in by the very fact that s/he is sitting in the same physical location as the machine and has access to all console functions. Therefore we cannot truly trust our workstations in the NFS interpretation of trust. To allow proper access controls in our environment we had to make some modifications to the base NFS software, and integrate Kerberos into the scheme.

Unmodified NFS

In the implementation of NFS that we started with (from the University of Wisconsin), authentication was provided in the form of a piece of data included in each NFS request (called a “credential” in NFS terminology). This credential contains information about the unique user identifier (UID) of the requester and a list of the group identifiers (GIDs) of the requester’s membership. This information is then used by the NFS server for access checking. The difference between a trusted and a non-trusted workstation is whether or not its credentials are accepted by the NFS server.12

Modified NFS

In our environment, NFS servers must accept credentials from a workstation if and only if the credentials indicate the UID of the workstation’s user, and no other.

One obvious solution would be to change the nature of credentials from mere indicators of UID and GIDs to full blown Kerberos authenticated data. However a significant performance penalty would be paid if this solution were adopted. Credentials are exchanged on every NFS operation including all disk read and write activities. Including a Kerberos authentication on each disk transaction would add a fair number of full-blown encryptions (done in software) per transaction and, according to our envelope calculations, would have delivered unacceptable performance. (It would also have required placing the Kerberos library routines in the kernel address space.)

We needed a hybrid approach, described below. The basic idea is to have the NFS server map credentials received from client workstations, to a valid (and possibly different) credential on the server system. This mapping is performed in the server’s kernel on each NFS transaction and is setup at “mount” time by a user-level process that engages in Kerberos-moderated authentication prior to establishing a valid kernel credential mapping.

To implement this we added a new system call to the kernel (required only on server systems, not on client systems) that provides for the control of the mapping function that maps incoming credentials from client workstations to credentials valid for use on the server (if any). The basic mapping function maps the tuple:

<CLIENT–IP–ADDRESS, UID–ON–CLIENT> to a valid NFS credential on the server system. The CLIENT–IP–ADDRESS is extracted from the NFS request packet and the UID–ON–CLIENT is extracted from the credential supplied by the client system. Note: all information in the client-generated credential except the UID–ON–CLIENT is discarded.

If no mapping exists, the server reacts in one of two ways, depending it is configured. In our friendly configuration we default the unmappable requests into the credentials for the user “nobody” who has no privileged access and has a unique UID. Unfriendly servers return an NFS access error when no valid mapping can be found for an incoming NFS credential.

Our new system call is used to add and delete entries from the kernel resident map. It also provides the ability to flush all entries that map to a specific UID on the server system, or flush all entries from a given CLIENT–IP–ADDRESS.

We modified the mount daemon (which handles NFS mount requests on server systems) to accept a new transaction type, the Kerberos authentication mapping request. Basically, as part of the mounting process, the client system provides a Kerberos authenticator along with an indication of her/his UID–ON–CLIENT (encrypted in the Kerberos authenticator) on the workstation. The server’s mount daemon converts the Kerberos principal name into a local username. This username is then looked up in a special file to yield the user’s UID and GIDs list. For efficiency, this file is a ndbm database file with the username as the key. From this information, an NFS credential is constructed and handed to the kernel as the valid mapping of the <CLIENT–IP–ADDRESS, CLIENT–UID> tuple for this request.

At unmount time a request is sent to the mount daemon to remove the previously added mapping from the kernel. It is also possible to send a request at logout time to invalidate all mapping for the current user on the server in question, thus cleaning up any remaining mappings that exist (though they shouldn’t) before the workstation is made available for the next user.

Security Implications of the Modified NFS

This implementation is not completely secure. For starters, user data is still sent across the network in an unencrypted, and therefore interceptable, form. The low-level, per-transaction authentication is based on a <CLIENT–IP–ADDRESS, CLIENT–UID> pair provided unencrypted in the request packet. This information could be forged and thus security compromised. However, it should be noted that only while a user is actively using her/his files (i.e., while logged in) are valid mappings in place and therefore this form of attack is limited to when the user in question is logged in. When a user is not logged in, no amount of IP address forgery will permit unauthorized access to her/his files.
