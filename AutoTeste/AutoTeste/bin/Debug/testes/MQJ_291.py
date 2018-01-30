







<!DOCTYPE html>
<html lang="en">
<head>
    







<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=Edge"/>
<title>Log in - JIRA</title>
<meta name="application-name" content="JIRA" data-name="jira" data-version="7.5.0"><meta name="ajs-dev-mode" content="false">
<meta name="ajs-context-path" content="/jira">
<meta name="ajs-version-number" content="7.5.0">
<meta name="ajs-build-number" content="75005">
<meta name="ajs-is-beta" content="false">
<meta name="ajs-is-rc" content="false">
<meta name="ajs-is-snapshot" content="false">
<meta name="ajs-is-milestone" content="false">
<meta name="ajs-remote-user" content="">
<meta name="ajs-remote-user-fullname" content="">
<meta name="ajs-user-locale" content="en_US">
<meta name="ajs-user-locale-group-separator" content=",">
<meta name="ajs-app-title" content="JIRA">
<meta name="ajs-keyboard-shortcuts-enabled" content="true">
<meta name="ajs-keyboard-accesskey-modifier" content="Alt">
<meta name="ajs-enabled-dark-features" content="[&quot;com.atlassian.jira.agile.darkfeature.editable.detailsview&quot;,&quot;nps.survey.inline.dialog&quot;,&quot;com.atlassian.jira.agile.darkfeature.edit.closed.sprint.enabled&quot;,&quot;jira.plugin.devstatus.phasetwo&quot;,&quot;jira.frother.reporter.field&quot;,&quot;atlassian.rest.xsrf.legacy.enabled&quot;,&quot;jira.issue.status.lozenge&quot;,&quot;com.atlassian.jira.config.BIG_PIPE&quot;,&quot;com.atlassian.jira.projects.issuenavigator&quot;,&quot;com.atlassian.jira.config.PDL&quot;,&quot;jira.plugin.devstatus.phasetwo.enabled&quot;,&quot;atlassian.aui.raphael.disabled&quot;,&quot;app-switcher.new&quot;,&quot;frother.assignee.field&quot;,&quot;com.atlassian.jira.projects.ProjectCentricNavigation.Switch&quot;,&quot;jira.onboarding.cyoa&quot;,&quot;com.atlassian.jira.agile.darkfeature.kanplan.enabled&quot;,&quot;sd.slavalue.record.updated.date.enabled&quot;,&quot;com.atlassian.jira.config.ProjectConfig.MENU&quot;,&quot;com.atlassian.jira.projects.sidebar.DEFER_RESOURCES&quot;,&quot;com.atlassian.jira.agile.darkfeature.kanplan.epics.and.versions.enabled&quot;,&quot;com.atlassian.jira.agile.darkfeature.sprint.goal.enabled&quot;,&quot;jira.zdu.admin-updates-ui&quot;,&quot;jira.zdu.jmx-monitoring&quot;,&quot;sd.sla.improved.rendering.enabled&quot;,&quot;sd.canned.responses.enabled&quot;,&quot;sd.new.settings.sidebar.location.disabled&quot;,&quot;jira.zdu.cluster-upgrade-state&quot;,&quot;com.atlassian.jira.agile.darkfeature.splitissue&quot;,&quot;com.atlassian.jira.config.CoreFeatures.LICENSE_ROLES_ENABLED&quot;,&quot;com.atlassian.feedback.feedback-button-move-to-header-enable&quot;,&quot;jira.export.csv.enabled&quot;]">
<meta name="ajs-in-admin-mode" content="false">
<meta name="ajs-is-sysadmin" content="false">
<meta name="ajs-is-admin" content="false">
<meta name="ajs-outgoing-mail-enabled" content="true">
<meta name="ajs-date-relativize" content="true">
<meta name="ajs-date-time" content="h:mm a">
<meta name="ajs-date-day" content="EEEE h:mm a">
<meta name="ajs-date-dmy" content="dd/MMM/yy">
<meta name="ajs-date-complete" content="dd/MMM/yy h:mm a">
<meta name="ajs-gebsun-authorized-projects-list" content="">
<meta name="ajs-gebsun-user" content="">
<meta name="ajs-gebsun-export-button-enabled" content="false">
<meta name="ajs-gebsun-current-server-issue-key" content="">
<meta name="ajs-gebsun-current-server-issue-permitted" content="$issuePermitted">
<meta name="ajs-gebsun-has-valid-license-flag" content="true"><script type="text/javascript">var AJS=AJS||{};AJS.debug=true;</script>


    
<meta id="atlassian-token" name="atlassian-token" content="BUQO-ZJD9-3O0R-JG52|af317c2c4bd1b49a2778e11a7549f1f7827241a3|lout">



<link rel="shortcut icon" href="/jira/s/-mou4xa/75005/b6b48b2829824b869586ac216d119363/_/favicon.ico">
<link rel="search" type="application/opensearchdescription+xml" href="/jira/osd.jsp" title="Log in - JIRA"/>

    



<!--[if IE]><![endif]-->
<script type="text/javascript">
    (function() {
        var contextPath = '/jira';
        var eventBuffer = [];

        function printDeprecatedMsg() {
            if (console && console.warn) {
                console.warn('DEPRECATED JS - contextPath global variable has been deprecated since 7.4.0. Use `wrm/context-path` module instead.');
            }
        }

        function sendEvent(analytics, postfix) {
            analytics.send({
                name: 'js.globals.contextPath.' + postfix
            });
        }

        function sendDeprecatedEvent(postfix) {
            try {
                var analytics = require('jira/analytics');
                if (eventBuffer.length) {
                    eventBuffer.forEach(function(value) {
                        sendEvent(analytics, value);
                    });
                    eventBuffer = [];
                }

                if (postfix) {
                    sendEvent(analytics, postfix);
                }
            } catch(ex) {
                eventBuffer.push(postfix);
                setTimeout(sendDeprecatedEvent, 1000);
            }
        }

        Object.defineProperty(window, 'contextPath', {
            get: function() {
                printDeprecatedMsg();
                sendDeprecatedEvent('get');
                return contextPath;
            },
            set: function(value) {
                printDeprecatedMsg();
                sendDeprecatedEvent('set');
                contextPath = value;
            }
        });
    })();

</script>
<script>
window.WRM=window.WRM||{};window.WRM._unparsedData=window.WRM._unparsedData||{};window.WRM._unparsedErrors=window.WRM._unparsedErrors||{};
WRM._unparsedData["com.atlassian.plugins.atlassian-plugins-webresource-plugin:context-path.context-path"]="\"/jira\"";
WRM._unparsedData["jira.webresources:feature-flags.feature-flag-data"]="{\"enabled-feature-keys\":[\"com.atlassian.jira.agile.darkfeature.editable.detailsview\",\"nps.survey.inline.dialog\",\"com.atlassian.jira.agile.darkfeature.edit.closed.sprint.enabled\",\"jira.plugin.devstatus.phasetwo\",\"jira.frother.reporter.field\",\"atlassian.rest.xsrf.legacy.enabled\",\"jira.issue.status.lozenge\",\"com.atlassian.jira.config.BIG_PIPE\",\"com.atlassian.jira.projects.issuenavigator\",\"com.atlassian.jira.config.PDL\",\"jira.plugin.devstatus.phasetwo.enabled\",\"atlassian.aui.raphael.disabled\",\"app-switcher.new\",\"frother.assignee.field\",\"com.atlassian.jira.projects.ProjectCentricNavigation.Switch\",\"jira.onboarding.cyoa\",\"com.atlassian.jira.agile.darkfeature.kanplan.enabled\",\"sd.slavalue.record.updated.date.enabled\",\"com.atlassian.jira.config.ProjectConfig.MENU\",\"com.atlassian.jira.projects.sidebar.DEFER_RESOURCES\",\"com.atlassian.jira.agile.darkfeature.kanplan.epics.and.versions.enabled\",\"com.atlassian.jira.agile.darkfeature.sprint.goal.enabled\",\"jira.zdu.admin-updates-ui\",\"jira.zdu.jmx-monitoring\",\"sd.sla.improved.rendering.enabled\",\"sd.canned.responses.enabled\",\"sd.new.settings.sidebar.location.disabled\",\"jira.zdu.cluster-upgrade-state\",\"com.atlassian.jira.agile.darkfeature.splitissue\",\"com.atlassian.jira.config.CoreFeatures.LICENSE_ROLES_ENABLED\",\"com.atlassian.feedback.feedback-button-move-to-header-enable\",\"jira.export.csv.enabled\"],\"feature-flag-states\":{\"sd.customer.profile.multi.languages\":true,\"sd.customer.portal.transitions\":true,\"sd.customer.portal.transitions.config\":true,\"sd.custom.email.stripping.rules\":false,\"sd.sla.lucene.issue.id.callback.performance\":true,\"sd.new.settings.sidebar.location\":true,\"sd.sla.wh.calendar.import\":false,\"sd.workload.report.paginator\":true,\"sd.experimental.portal.search.algorithm.default.1\":false,\"sd.customer.portal.help.center.agent.announcement\":true,\"sd.sla.improved.rendering\":false,\"sd.experimental.portal.search.algorithm.default.2\":false,\"sd.customer.feedback.validate.reporter.on.token\":true,\"sd.custom.email.notifications.utf8.csat.star\":true,\"sd.who.create.customers.by.email.setting\":true,\"sd.stats.event.tracking\":true,\"sd.password.helper.dialog\":true,\"sd.canned.responses\":false,\"sd.portal.help.center.customer.signup.secondary.email\":true,\"sd.custom.email.notifications.manage.language\":true,\"sd.use.search.by.permissions\":true,\"sd.slavalue.record.updated.date\":false,\"sd.report.custom.date.range\":false,\"sd.kb.article.helpfulness.report\":false,\"com.atlassian.jira.agile.darkfeature.sprint.goal\":false,\"sd.custom.email.notifications.styling\":true,\"sd.customer.portal.two.step.login\":false,\"sd.automation.psmq.async.executor\":true,\"sd.customer.org.list.page.lazy.search\":true,\"sd.approval.requested.when.handler\":true,\"sd.request.type.field.rest.api.filtering.bugfix\":true,\"sd.automation.then.action.auto.answer.approval\":false,\"com.atlassian.jira.agile.darkfeature.kanplan.epics.and.versions\":false,\"sla.will.only.be.paused.if.they.are.already.started\":true,\"sd.kb.comment.share.stats.collection\":true,\"com.atlassian.jira.upgrade.startup.fix.index\":true,\"sd.customer.orgs.group.participants\":true,\"sd.portal.help.center.customer.signup\":true,\"sd.sla.agent.jql.security.restricted\":true,\"sd.test.feature.flag.x\":true,\"sd.test.feature.flag.y\":false,\"sd.cluster.safe.mail.channel.shutdown\":true,\"sd.email.channel.folders\":false,\"sd.email.analytics.open\":false,\"sd.kb.project.creation.create.link.space\":true,\"sd.confluence.anonymous.permission.fix\":true,\"sd.customer.portal.project.agent.announcement\":true,\"sd.automation.audit.log\":true,\"jira.jql.suggestrecentfields\":false,\"sd.canned.responses.check.index.startup\":false,\"sd.new.project.templates\":true,\"sd.custom.email.notifications.custom.rules.simple.ui\":false,\"sd.custom.email.notifications.cut.over\":true,\"sd.sla.configurations.export\":true,\"sd.canned.responses.variable.substitution\":false,\"com.atlassian.jira.agile.darkfeature.kanplan\":false,\"jira.instrumentation.laas\":false,\"sd.kb.self.service.report\":false,\"sd.no.schedule.async.upgrade.tasks\":false,\"sd.kb.primary.nav\":true,\"com.atlassian.jira.agile.darkfeature.edit.closed.sprint\":false,\"sd.kb.issueview.panel.phase2\":true,\"sd.email.outsider.comments\":true,\"jira.create.linked.issue\":true,\"sd.kb.issueview.panel\":true,\"jira.sal.host.connect.accessor.existing.transaction.will.create.transactions\":true,\"sd.approvals.light.weight\":false,\"sd.automation.then.webhook\":true,\"sd.respect.inline.edit.issue.off\":true,\"jira.jql.smartautoselectfirst\":false,\"sd.global.portal.search.atlassian.only.tracking\":false,\"sd.automation.if.condition.comment.primary.action\":true,\"sd.sla.workinghours.querydsl\":true,\"sd.customer.request.type.create.edit.screens\":true}}";
WRM._unparsedData["jira.webresources:default-comment-security-level.DefaultCommentSecurityLevelHelpLink"]="{\"extraClasses\":\"default-comment-level-help\",\"title\":\"Commenting on an Issue\",\"url\":\"https://docs.atlassian.com/jira/jcore-docs-075/Editing+and+collaborating+on+issues#Editingandcollaboratingonissues-restrictacomment\",\"isLocal\":false}";
WRM._unparsedData["com.atlassian.analytics.analytics-client:policy-update-init.policy-update-data-provider"]="false";
WRM._unparsedData["com.atlassian.analytics.analytics-client:programmatic-analytics-init.programmatic-analytics-data-provider"]="false";
WRM._unparsedData["com.onresolve.jira.groovy.groovyrunner:web-item-response-renderer.web-item-actions-data-provider"]="[]";
WRM._unparsedData["jira.webresources:dateFormatProvider.allFormats"]="{\"dateFormats\":{\"meridiem\":[\"AM\",\"PM\"],\"eras\":[\"BC\",\"AD\"],\"months\":[\"January\",\"February\",\"March\",\"April\",\"May\",\"June\",\"July\",\"August\",\"September\",\"October\",\"November\",\"December\"],\"monthsShort\":[\"Jan\",\"Feb\",\"Mar\",\"Apr\",\"May\",\"Jun\",\"Jul\",\"Aug\",\"Sep\",\"Oct\",\"Nov\",\"Dec\"],\"weekdaysShort\":[\"Sun\",\"Mon\",\"Tue\",\"Wed\",\"Thu\",\"Fri\",\"Sat\"],\"weekdays\":[\"Sunday\",\"Monday\",\"Tuesday\",\"Wednesday\",\"Thursday\",\"Friday\",\"Saturday\"]},\"lookAndFeelFormats\":{\"relativize\":\"true\",\"time\":\"h:mm a\",\"day\":\"EEEE h:mm a\",\"dmy\":\"dd/MMM/yy\",\"complete\":\"dd/MMM/yy h:mm a\"}}";
WRM._unparsedData["com.atlassian.servicedesk.servicedesk-canned-responses-plugin:canned-responses-data-provider.data"]="{}";
WRM._unparsedData["jira.webresources:avatar-picker.data"]="{}";
WRM._unparsedData["com.atlassian.feedback.jira-feedback-plugin:button-resources-init.data"]="{\"jira.feedback.plugin.issue.collector.core\":\"https://jira.atlassian.com/s/576e9ab86257d4f65f6ea5b6dd50de44-T/en_UK3ljiw5/71006/b6b48b2829824b869586ac216d119363/2.0.11/_/download/batch/com.atlassian.jira.collector.plugin.jira-issue-collector-plugin:issuecollector-embededjs/com.atlassian.jira.collector.plugin.jira-issue-collector-plugin:issuecollector-embededjs.js?locale=en-UK&collectorId=abbf546d\",\"jira.feedback.plugin.issue.collector.default\":\"https://jira.atlassian.com/s/576e9ab86257d4f65f6ea5b6dd50de44-T/en_UK3ljiw5/71006/b6b48b2829824b869586ac216d119363/2.0.11/_/download/batch/com.atlassian.jira.collector.plugin.jira-issue-collector-plugin:issuecollector-embededjs/com.atlassian.jira.collector.plugin.jira-issue-collector-plugin:issuecollector-embededjs.js?locale=en-UK&collectorId=abbf546d\",\"jira.feedback.plugin.issue.collector.service.desk\":\"https://jira.atlassian.com/s/576e9ab86257d4f65f6ea5b6dd50de44-T/en_UK3ljiw5/71006/b6b48b2829824b869586ac216d119363/2.0.11/_/download/batch/com.atlassian.jira.collector.plugin.jira-issue-collector-plugin:issuecollector/com.atlassian.jira.collector.plugin.jira-issue-collector-plugin:issuecollector.js?locale=en-UK&collectorId=a698db21\",\"jira.feedback.plugin.issue.collector.software\":\"https://jira.atlassian.com/s/576e9ab86257d4f65f6ea5b6dd50de44-T/en_UK3ljiw5/71006/b6b48b2829824b869586ac216d119363/2.0.11/_/download/batch/com.atlassian.jira.collector.plugin.jira-issue-collector-plugin:issuecollector-embededjs/com.atlassian.jira.collector.plugin.jira-issue-collector-plugin:issuecollector-embededjs.js?locale=en-UK&collectorId=abbf546d\",\"isHeaderFeedbackButtonEnabled\":true}";
WRM._unparsedData["com.atlassian.jira.jira-header-plugin:dismissedFlags.flags"]="{\"dismissed\":[]}";
WRM._unparsedData["com.atlassian.jira.jira-header-plugin:newsletter-signup-tip-init.newsletterSignup"]="{\"signupDescription\":\"Get updates, inspiration and best practices from the team behind JIRA.\",\"formUrl\":\"https://www.atlassian.com/apis/exact-target/{0}/subscribe?mailingListId=1401671\",\"signupTitle\":\"Sign up!\",\"signupId\":\"newsletter-signup-tip\",\"showNewsletterTip\":false}";
WRM._unparsedData["com.atlassian.jira.project-templates-plugin:project-templates-plugin-resources.ptAnalyticsData"]="{\"instanceCreatedDate\":\"2015-10-06\"}";
WRM._unparsedData["jira.webresources:jqlautocomplete.jql.autocomplete.recentFields"]="{\"key\":\"jqlValues\",\"value\":[\"affectedVersion\",\"assignee\",\"component\",\"description\",\"issue\",\"labels\",\"parent\",\"priority\",\"project\",\"reporter\",\"resolution\",\"status\",\"summary\",\"type\",\"watcher\"]}";
WRM._unparsedData["com.atlassian.servicedesk.core-ui:util-help-links.help-links"]="{\"help\":{\"email.settings\":\"https://docs.atlassian.com/jira/jsd-docs-038/Receiving+requests+by+email\",\"managing.queues\":\"https://docs.atlassian.com/jira/jsd-docs-038/Setting+up+queues+for+your+team\",\"email.setup\":\"https://docs.atlassian.com/jira/jsd-docs-038/Receiving+requests+by+email\",\"request.settings.help.bubble\":\"https://docs.atlassian.com/jira/jsd-docs-038/Managing+access+to+your+service+desk\",\"email.settings.suitablerequest\":\"https://docs.atlassian.com/jira/jsd-docs-038/Receiving+requests+by+email#Receivingrequestsbyemail-suitablerequest\",\"sla.import.help\":\"https://docs.atlassian.com/jira/jsd-docs-038/Importing+SLAs\",\"documentation.home\":\"https://docs.atlassian.com/jira/jsd-docs-038/JIRA+Service+Desk+Documentation\",\"default\":\"https://docs.atlassian.com/jira/jsd-docs-038/\",\"create.space.help\":\"https://docs.atlassian.com/jira/jsd-docs-038/Serving+customers+with+a+knowledge+base#serving-customers-with-a-knowledge-base-createpermission\",\"email.settings.troubleshooting\":\"https://docs.atlassian.com/jira/jsd-docs-038/Troubleshooting+issues+with+the+email+channel\",\"admin.notifications.config\":\"https://docs.atlassian.com/jira/jsd-docs-038/Managing+service+desk+notifications\",\"troubleshoot.requesttype\":\"https://docs.atlassian.com/jira/jsd-docs-038/Troubleshooting+issues+with+request+types\",\"approvals.configuration\":\"https://docs.atlassian.com/jira/jsd-docs-038/Configuring+JIRA+Service+Desk+approvals\",\"setting.up.reports\":\"https://docs.atlassian.com/jira/jsd-docs-038/Setting+up+service+desk+reports\",\"public.signup\":\"https://docs.atlassian.com/jira/jsd-docs-038/Configuring+public+signup\",\"knowledge.base\":\"https://docs.atlassian.com/jira/jsd-docs-038/Serving+customers+with+a+knowledge+base\",\"resolve.permission.scheme.errors\":\"https://docs.atlassian.com/jira/jsd-docs-038/Resolving+permission+scheme+errors\",\"getting.started\":\"https://docs.atlassian.com/jira/jsd-docs-038/Getting+started+with+JIRA+Service+Desk\",\"getting.started.agent\":\"https://docs.atlassian.com/jira/jsd-docs-038/Getting+started+for+service+desk+agents\",\"invite.customers\":\"https://docs.atlassian.com/jira/jsd-docs-038/Managing+access+to+your+service+desk\"},\"kb\":{\"default\":\"https://confluence.atlassian.com/display/SDKB/\",\"troubleshooting.user.management.issues\":\"https://confluence.atlassian.com/display/SDKB/Troubleshooting+issues+with+service+desk+user+management\",\"legacytransition\":\"https://confluence.atlassian.com/display/SDKB/Replacing+legacy+automatic+transitions+with+automation+rules\",\"umtroubleshoot\":\"https://confluence.atlassian.com/display/SDKB/Troubleshooting+issues+with+service+desk+user+management\"}}";
WRM._unparsedData["com.atlassian.servicedesk.core-ui:util-base-url.base-url"]="\"http://jira.inatel.br/jira\"";
WRM._unparsedData["com.atlassian.jira.plugins.jira-wiki-editor:wiki-editor-resources.help-data"]="{\"showHelp\":true,\"editorDocumentationUrl\":[\"https://docs.atlassian.com/jira/jcore-docs-075/Visual+editing\"],\"editorDocumentationTitle\":[\"Show me documentation for the visual editor\"]}";
WRM._unparsedData["com.atlassian.jira.plugins.jira-wiki-editor:wiki-editor-resources.thumbnails-allowed"]="true";
WRM._unparsedData["jira.webresources:user-message-flags.adminLockout"]="{}";
WRM._unparsedData["com.atlassian.plugins.helptips.jira-help-tips:help-tip-manager.JiraHelpTipData"]="{\"anonymous\":true}";
WRM._unparsedData["jira.request.correlation-id"]="\"9a050efc664976\"";
if(window.WRM._dataArrived)window.WRM._dataArrived();</script>
<link type="text/css" rel="stylesheet" href="/jira/s/b6f9064bf821e041adea82410d97c909-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/aa6cf545ff213915ecbf1d6cdcbaa2cc/_/download/contextbatch/css/_super/batch.css" data-wrm-key="_super" data-wrm-batch-type="context" media="all">
<link type="text/css" rel="stylesheet" href="/jira/s/baf372822ec7497efdb336037c0995b5-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/7c2f4572942b152e95f136bdfff31a63/_/download/contextbatch/css/atl.general,jira.global,atl.global,jira.general,-_super/batch.css?agile_global_admin_condition=true&amp;hc-enabled=true&amp;is-server-instance=true&amp;jag=true&amp;jcap=true&amp;nps-acknowledged=true&amp;sd_operational=true&amp;tempo_is_jira_version_equal_or_greater_than_7.0.0=true&amp;tempo_is_tempo_core_licensed=true&amp;tempo_is_tempo_timesheets_license_valid=false" data-wrm-key="atl.general,jira.global,atl.global,jira.general,-_super" data-wrm-batch-type="context" media="all">
<link type="text/css" rel="stylesheet" href="/jira/s/26479f0df4da0467b316ef6ea0377543-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/2c47a096316a1ea6dd4061883ffb678a/_/download/contextbatch/css/jira.login,-_super/batch.css" data-wrm-key="jira.login,-_super" data-wrm-batch-type="context" media="all">
<link type="text/css" rel="stylesheet" href="/jira/s/26479f0df4da0467b316ef6ea0377543-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/1.0/_/download/batch/jira.webresources:captcha/jira.webresources:captcha.css" data-wrm-key="jira.webresources:captcha" data-wrm-batch-type="resource" media="all">
<link type="text/css" rel="stylesheet" href="/jira/s/d41d8cd98f00b204e9800998ecf8427e-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/4.3.0/_/download/batch/com.tempoplugin.tempo-core:tempo-core/com.tempoplugin.tempo-core:tempo-core.css" data-wrm-key="com.tempoplugin.tempo-core:tempo-core" data-wrm-batch-type="resource" media="all">
<link type="text/css" rel="stylesheet" href="/jira/s/0e5604f912273ef185ac02e47b9a1bbb-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/6.0.0/_/download/batch/com.atlassian.auiplugin:aui-date-picker/com.atlassian.auiplugin:aui-date-picker.css" data-wrm-key="com.atlassian.auiplugin:aui-date-picker" data-wrm-batch-type="resource" media="all">
<link type="text/css" rel="stylesheet" href="/jira/s/d41d8cd98f00b204e9800998ecf8427e-T/-mou4xa/75005/b6b48b2829824b869586ac216d119363/4.3.0/_/download/batch/com.tempoplugin.tempo-core:core-issue-expense-resource/com.tempoplugin.tempo-core:core-issue-expense-resource.css" data-wrm-key="com.tempoplugin.tempo-core:core-issue-expense-resource" data-wrm-batch-type="resource" media="all">
<link type="text/css" rel="stylesheet" href="/jira/s/35fda08f7840053ac68fa9cc801b15f3-T/-mou4xa/75005/b6b48b2829824b869586ac216d119363/7.5.0/_/download/batch/com.atlassian.feedback.jira-feedback-plugin:button-resources-init/com.atlassian.feedback.jira-feedback-plugin:button-resources-init.css" data-wrm-key="com.atlassian.feedback.jira-feedback-plugin:button-resources-init" data-wrm-batch-type="resource" media="all">
<script type="text/javascript" src="/jira/s/94d8fa893c904da1d7e58e737a2cb180-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/aa6cf545ff213915ecbf1d6cdcbaa2cc/_/download/contextbatch/js/_super/batch.js?locale=en-US" data-wrm-key="_super" data-wrm-batch-type="context" data-initially-rendered></script>
<script type="text/javascript" src="/jira/s/a5e3b419426698f224bd9a6fbe900df7-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/7c2f4572942b152e95f136bdfff31a63/_/download/contextbatch/js/atl.general,jira.global,atl.global,jira.general,-_super/batch.js?agile_global_admin_condition=true&amp;hc-enabled=true&amp;is-server-instance=true&amp;jag=true&amp;jcap=true&amp;locale=en-US&amp;nps-acknowledged=true&amp;sd_operational=true&amp;tempo_is_jira_version_equal_or_greater_than_7.0.0=true&amp;tempo_is_tempo_core_licensed=true&amp;tempo_is_tempo_timesheets_license_valid=false" data-wrm-key="atl.general,jira.global,atl.global,jira.general,-_super" data-wrm-batch-type="context" data-initially-rendered></script>
<script type="text/javascript" src="/jira/s/d41d8cd98f00b204e9800998ecf8427e-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/1.0/_/download/batch/jira.webresources:captcha/jira.webresources:captcha.js" data-wrm-key="jira.webresources:captcha" data-wrm-batch-type="resource" data-initially-rendered></script>
<script type="text/javascript" src="/jira/s/d41d8cd98f00b204e9800998ecf8427e-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/4.3.0/_/download/batch/com.tempoplugin.tempo-core:tempo-moment/com.tempoplugin.tempo-core:tempo-moment.js" data-wrm-key="com.tempoplugin.tempo-core:tempo-moment" data-wrm-batch-type="resource" data-initially-rendered></script>
<script type="text/javascript" src="/jira/s/74b2b146be383b28bfda8370df64a8db-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/4.3.0/_/download/batch/com.tempoplugin.tempo-core:core-global-constants-resource/com.tempoplugin.tempo-core:core-global-constants-resource.js?locale=en-US" data-wrm-key="com.tempoplugin.tempo-core:core-global-constants-resource" data-wrm-batch-type="resource" data-initially-rendered></script>
<script type="text/javascript" src="/jira/s/74b2b146be383b28bfda8370df64a8db-T/-mou4xa/75005/b6b48b2829824b869586ac216d119363/4.3.0/_/download/batch/com.tempoplugin.tempo-core:core-expense-backbone-resource/com.tempoplugin.tempo-core:core-expense-backbone-resource.js?locale=en-US" data-wrm-key="com.tempoplugin.tempo-core:core-expense-backbone-resource" data-wrm-batch-type="resource" data-initially-rendered></script>
<script type="text/javascript" src="/jira/s/74b2b146be383b28bfda8370df64a8db-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/6.0.0/_/download/batch/com.atlassian.auiplugin:internal-@atlassian-aui-src-js-vendor-jquery-jquery-ui-jquery-ui-datepicker/com.atlassian.auiplugin:internal-@atlassian-aui-src-js-vendor-jquery-jquery-ui-jquery-ui-datepicker.js?locale=en-US" data-wrm-key="com.atlassian.auiplugin:internal-@atlassian-aui-src-js-vendor-jquery-jquery-ui-jquery-ui-datepicker" data-wrm-batch-type="resource" data-initially-rendered></script>
<script type="text/javascript" src="/jira/s/74b2b146be383b28bfda8370df64a8db-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/6.0.0/_/download/batch/com.atlassian.auiplugin:internal-@atlassian-aui-src-js-aui-date-picker/com.atlassian.auiplugin:internal-@atlassian-aui-src-js-aui-date-picker.js?locale=en-US" data-wrm-key="com.atlassian.auiplugin:internal-@atlassian-aui-src-js-aui-date-picker" data-wrm-batch-type="resource" data-initially-rendered></script>
<script type="text/javascript" src="/jira/s/d41d8cd98f00b204e9800998ecf8427e-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/6.0.0/_/download/batch/com.atlassian.auiplugin:internal-jquery-ui-datepicker/com.atlassian.auiplugin:internal-jquery-ui-datepicker.js" data-wrm-key="com.atlassian.auiplugin:internal-jquery-ui-datepicker" data-wrm-batch-type="resource" data-initially-rendered></script>
<script type="text/javascript" src="/jira/s/68af83ba567bea49f051bdc08c6d7d46-T/-mou4xa/75005/b6b48b2829824b869586ac216d119363/4.3.0/_/download/batch/com.tempoplugin.tempo-core:core-expense-resource/com.tempoplugin.tempo-core:core-expense-resource.js?locale=en-US" data-wrm-key="com.tempoplugin.tempo-core:core-expense-resource" data-wrm-batch-type="resource" data-initially-rendered></script>
<script type="text/javascript" src="/jira/s/68af83ba567bea49f051bdc08c6d7d46-T/-mou4xa/75005/b6b48b2829824b869586ac216d119363/4.3.0/_/download/batch/com.tempoplugin.tempo-core:core-issue-expense-resource/com.tempoplugin.tempo-core:core-issue-expense-resource.js?locale=en-US" data-wrm-key="com.tempoplugin.tempo-core:core-issue-expense-resource" data-wrm-batch-type="resource" data-initially-rendered></script>
<script type="text/javascript" src="/jira/s/d41d8cd98f00b204e9800998ecf8427e-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/4.5.6/_/download/batch/com.atlassian.jira.jira-projects-plugin:data/com.atlassian.jira.jira-projects-plugin:data.js" data-wrm-key="com.atlassian.jira.jira-projects-plugin:data" data-wrm-batch-type="resource" data-initially-rendered></script>
<script type="text/javascript" src="/jira/s/d41d8cd98f00b204e9800998ecf8427e-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/4.5.6/_/download/batch/com.atlassian.jira.jira-projects-plugin:projects-api/com.atlassian.jira.jira-projects-plugin:projects-api.js" data-wrm-key="com.atlassian.jira.jira-projects-plugin:projects-api" data-wrm-batch-type="resource" data-initially-rendered></script>
<script type="text/javascript" src="/jira/s/d41d8cd98f00b204e9800998ecf8427e-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/7.5.0/_/download/batch/com.atlassian.feedback.jira-feedback-plugin:button-resources/com.atlassian.feedback.jira-feedback-plugin:button-resources.js" data-wrm-key="com.atlassian.feedback.jira-feedback-plugin:button-resources" data-wrm-batch-type="resource" data-initially-rendered></script>
<link type="text/css" rel="stylesheet" href="/jira/s/44b511b079218a635194ce1cf83abd67-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/3945adba647b1b9df896cf5aab0177b6/_/download/contextbatch/css/jira.global.look-and-feel,-_super/batch.css" data-wrm-key="jira.global.look-and-feel,-_super" data-wrm-batch-type="context" media="all">

<script type="text/javascript" src="/jira/rest/api/1.0/shortcuts/75005/d499ca8308039cdbd4ad1a963637b806/shortcuts.js"></script>


    <meta name="viewport" content="width=device-width, minimum-scale=1, initial-scale=1, maximum-scale=1, user-scalable=no">
    
	
    <meta name="decorator" content="login" />

</head>
<body id="jira" class="aui-layout aui-theme-default page-type-login  " data-version="7.5.0">
    <div id="page">
        
            <header id="header" role="banner">
                






<script>
require(["jquery", "jira/license-banner"], function ($, licenseBanner) {
    $(function () {
        licenseBanner.showLicenseBanner("");
        licenseBanner.showLicenseFlag("");
    });
});
</script>



                




                




<nav class="aui-header aui-dropdown2-trigger-group" role="navigation"><div class="aui-header-inner"><div class="aui-header-before"><a class=" aui-dropdown2-trigger app-switcher-trigger" aria-controls="app-switcher" aria-haspopup="true" role="button" tabindex="0" data-aui-trigger href="#app-switcher"><span class="aui-icon aui-icon-small aui-iconfont-appswitcher">Linked Applications</span></a><div id="app-switcher" class="aui-dropdown2 aui-style-default" role="menu" aria-hidden="true" data-is-switcher="true" data-environment="{&quot;isUserAdmin&quot;:false,&quot;isAppSuggestionAvailable&quot;:false,&quot;isSiteAdminUser&quot;:false}"><div role="application"><div class="app-switcher-loading">Loading&hellip;</div></div></div></div><div class="aui-header-primary"><h1 id="logo" class="aui-header-logo aui-header-logo-custom"><a href="http://jira.inatel.br/jira/secure/MyJiraHome.jspa"><img src="/jira/s/-mou4xa/75005/b6b48b2829824b869586ac216d119363/_/images/icon-jira-logo.png" alt="JIRA" /></a></h1><ul class='aui-nav'><li><a href="/jira/secure/Dashboard.jspa" class=" aui-nav-link aui-dropdown2-trigger aui-dropdown2-ajax" id="home_link" aria-haspopup="true" aria-controls="home_link-content" title="View and manage your dashboards" accesskey="d">Dashboards</a><div class="aui-dropdown2 aui-style-default" id="home_link-content" data-aui-dropdown2-ajax-key="home_link"></div></li><li><a href="/jira/secure/SessionNavigator.jspa" class=" aui-nav-link aui-dropdown2-trigger" id="bonfire_top_menu_dropdown" aria-haspopup="true" aria-controls="bonfire_top_menu_dropdown-content" title="Capture">Capture</a><div class="aui-dropdown2 aui-style-default" id="bonfire_top_menu_dropdown-content"><div id="bonfire_top_main_menu.2" class="aui-dropdown2-section" ><ul class="aui-list-truncate"><li id="bonfire_gettingstarted_link"><a href="/jira/secure/BonfireGettingStarted.jspa" id="bonfire_gettingstarted_link_lnk" class="">Getting started</a></li></ul></div></div></li>
</ul></div><div class="aui-header-secondary"><ul class='aui-nav'><li id="quicksearch-menu">
    <form action="/jira/secure/QuickSearch.jspa" method="get" id="quicksearch" class="aui-quicksearch dont-default-focus ajs-dirty-warning-exempt">
        <input id="quickSearchInput" class="search" type="text" title="Search" placeholder="Search" name="searchString" accessKey="q" />
        <input type="submit" class="hidden" value="Search">
    </form>
</li>
<li><a class="jira-feedback-plugin" role="button" aria-haspopup="true" id="jira-header-feedback-link" href="#"><span class="aui-icon aui-icon-small jira-feedback-plugin-icon">Give feedback to Atlassian</span></a></li>



    <li id="system-help-menu">
        <a class="aui-nav-link aui-dropdown2-trigger" id="help_menu" aria-haspopup="true" aria-owns="system-help-menu-content" href="https://docs.atlassian.com/jira/jcore-docs-075/"  target="$textUtils.htmlEncode($rootHelpMenuItem.params.target)"  title="Help"><span class="aui-icon aui-icon-small aui-iconfont-help">Help</span></a>
        <div id="system-help-menu-content" class="aui-dropdown2 aui-style-default">
                            <div class="aui-dropdown2-section">
                                                                <ul id="jira-help" class="aui-list-truncate">
                                                            <li>
                                    <a id="view_core_help" class="aui-nav-link " title="Go to the online documentation for JIRA Core" href="https://docs.atlassian.com/jira/jcore-docs-075/"  target="_blank" >JIRA Core help</a>
                                </li>
                                                            <li>
                                    <a id="keyshortscuthelp" class="aui-nav-link " title="Get more information about JIRA's Keyboard Shortcuts" href="/jira/secure/ViewKeyboardShortcuts!default.jspa"  target="_blank" >Keyboard Shortcuts</a>
                                </li>
                                                            <li>
                                    <a id="view_about" class="aui-nav-link " title="Get more information about JIRA" href="/jira/secure/AboutPage.jspa" >About JIRA</a>
                                </li>
                                                            <li>
                                    <a id="view_credits" class="aui-nav-link " title="See who did what" href="/jira/secure/JiraCreditsPage!default.jspa"  target="_blank" >JIRA Credits</a>
                                </li>
                                                            <li>
                                    <a id="tempo_core_help" class="aui-nav-link " title="Goto the online documentation for Tempo" href="https://tempoplugin.jira.com/wiki/display/TD/Tempo+Documentation" target="_blank" >Tempo Help</a>
                                </li>
                                                    </ul>
                                    </div>
                    </div>
    </li>









<li id="user-options">
            <a class="aui-nav-link login-link" href="/jira/login.jsp?os_destination=%2Fsecure%2Fattachment%2F19064%2FMQJ_291.py">Log In</a>
                <div id="user-options-content" class="aui-dropdown2 aui-style-default">
                            <div class="aui-dropdown2-section">
                                                        </div>
                    </div>
    </li>
</ul></div></div><!-- .aui-header-inner--></nav><!-- .aui-header -->
            </header>
        
        



        <section id="content" role="main">
            <div class="aui-page-panel"><div class="aui-page-panel-inner">
                    <section class="aui-page-panel-content">
                            
    
        <header class="aui-page-header"><div class="aui-page-header-inner"><div class="aui-page-header-main">
                <h1>Welcome to JIRA</h1>
            </div></div></header>
    
    
































<form action="/jira/login.jsp"
      class="aui"
      
      id="login-form"
      method="post">
    <div class="form-body">
        
        
        
        
        
    
    
    
    

    
        
                
                
        
    

    

    
    











<div class="aui-message warning"><span class="aui-icon icon-warning"></span>
        

        
        
        
            <p>You must log in to access this page.</p>
        

        
            <p>
                If you think this message is wrong, please contact your JIRA administrators.
            </p>
        
        </div>









    

    
    <div class="aui-group jira-login-method">
        <div class="aui-item jira-login-item">
        




<div class="field-group">
    
            <label accesskey="u" for="login-form-username"><u>U</u>sername</label>
            <input class="text medium-field" id="login-form-username" name="os_username" type="text" value="" />
        
    
</div>

        




<div class="field-group">
    
            <label accesskey="p" for="login-form-password" id="passwordlabel"><u>P</u>assword</label>
            <input id="login-form-password" class="text medium-field" name="os_password" type="password" />
        
    
</div>

        
        
            




<fieldset class="group ">
    
    
                
                




<div class="checkbox">
    
                    
                    <input class="checkbox" id="login-form-remember-me" name="os_cookie" type="checkbox" value="true" />
                    <label for="login-form-remember-me" accesskey="r"><u>R</u>emember my login on this computer</label>
                
    
</div>
            
</fieldset> <!-- // .group -->
        
        

        
        
            <div id="sign-up-hint" class="field-group">
                
                Not a member? To request an account, please contact your JIRA administrators.
                
            </div>
        
        </div>
    </div>
    


<div class="hidden"
     
            
     
    >
    <input
        
            
        
        
            name="os_destination"
        
        type="hidden"
        
            value="/secure/attachment/19064/MQJ_291.py"
            
        
        
            
        
    />
</div>

    
    


<div class="hidden"
     
            
     
    >
    <input
        
            
        
        
            name="user_role"
        
        type="hidden"
        
            
            
        
        
            
        
    />
</div>


        
        


<div class="hidden"
     
            
     
    >
    <input
        
            
        
        
            name="atl_token"
        
        type="hidden"
        
            
            
        
        
            
        
    />
</div>

    </div>
    
    <div class="buttons-container form-footer">
        <div class="buttons">
            
                




<input
    
        accesskey="s"
    
    
        
        class="aui-button"
    
    
    
        id="login-form-submit"
    
    
    name="login"
    title="Press Alt+s to submit this form"
    type="submit"
    
        value="Log In"
        
    
    />

            
            
                


<a
    
    accesskey="`"
    
    
        
        class="aui-button aui-button-link cancel"
    
    href="/jira/secure/ForgotLoginDetails.jspa"
    id="login-form-cancel"
    title="Press Alt+` to cancel"
>Can&#39;t access your account?</a>
            
        </div>
        
    </div>
    
</form> <!-- // .aui #login-form -->




                        </section><!-- .aui-page-panel-content -->
                </div><!-- .aui-page-panel-inner --></div><!-- .aui-page-panel -->
        </section>
        
            <footer id="footer" role="contentinfo">
                
                

<section class="footer-body">
<ul class="atlassian-footer">
    <li>
        Atlassian JIRA <a class="seo-link" rel="nofollow" href="https://www.atlassian.com/software/jira">Project Management Software</a>
                                            <span id="footer-build-information">(v7.5.0#75005-<span title='fd8c849d4e278dd8bbaccc61e707a716ad697024' data-commit-id='fd8c849d4e278dd8bbaccc61e707a716ad697024}'>sha1:fd8c849</span>)</span>
    </li>
    <li>
        <a id="about-link" rel="nofollow" href="/jira/secure/AboutPage.jspa/secure/AboutPage.jspa">About JIRA</a>
    </li>
    <li>
        <a id="footer-report-problem-link" rel="nofollow" href="/jira/secure/CreateIssue!default.jspa">Report a problem</a>
    </li>
</ul>
    <ul class="atlassian-footer">
        <li class="licensemessage">
                Powered by a free Atlassian <a rel='nofollow' href='http://www.atlassian.com/software/jira'>JIRA</a> community license for Fundação Instituto Nacional de Telecomunicações. Try JIRA - <a rel='nofollow' href='http://www.atlassian.com/software/jira'>bug tracking software</a> for <i>your</i> team.

        </li>
    </ul>

    <div id="footer-logo"><a rel="nofollow" href="http://www.atlassian.com/">Atlassian</a></div>
</section>











<fieldset class="hidden parameters">
    <input type="hidden" title="loggedInUser" value="">
    <input type="hidden" title="ajaxTimeout" value="The call to the JIRA server did not complete within the timeout period.  We are unsure of the result of this operation.">
    <input type="hidden" title="JiraVersion" value="7.5.0" />
    <input type="hidden" title="ajaxUnauthorised" value="You are not authorized to perform this operation.  Please log in.">
    <input type="hidden" title="baseURL" value="http://jira.inatel.br/jira" />
    <input type="hidden" title="ajaxCommsError" value="The JIRA server could not be contacted. This may be a temporary glitch or the server may be down. ">
    <input type="hidden" title="ajaxServerError" value="The JIRA server was contacted but has returned an error response. We are unsure of the result of this operation.">
    <input type="hidden" title="ajaxErrorCloseDialog" value="Close this dialog and press refresh in your browser">
    <input type="hidden" title="ajaxErrorDialogHeading" value="Communications Breakdown">

    <input type="hidden" title="dirtyMessage" value="You have entered new data on this page. If you navigate away from this page without first saving your data, the changes will be lost.">
    <input type="hidden" title="dirtyDialogMessage" value="You have entered new data in this dialog. If you navigate away from this dialog without first saving your data, the changes will be lost. Click cancel to return to the dialog.">
    <input type="hidden" title="keyType" value="Type">
    <input type="hidden" title="keyThen" value="then">
    <input type="hidden" title="dblClickToExpand" value="Double click to expand">
    <input type="hidden" title="actions" value="Actions">
    <input type="hidden" title="removeItem" value="Remove">
    <input type="hidden" title="workflow" value="Workflow">
    <input type="hidden" title="labelNew" value="New Label">
    <input type="hidden" title="issueActionsHint" value="Begin typing for available operations or press down to see all">
    <input type="hidden" title="closelink" value="Close">
    <input type="hidden" title="dotOperations" value="Operations">
    <input type="hidden" title="dotLoading" value="Loading...">
    <input type="hidden" title="frotherSuggestions" value="Suggestions">
    <input type="hidden" title="frotherNomatches" value="No Matches">
    <input type="hidden" title="multiselectVersionsError" value="{0} is not a valid version.">
    <input type="hidden" title="multiselectComponentsError" value="{0} is not a valid component.">
    <input type="hidden" title="multiselectGenericError" value="The value {0} is invalid.">
</fieldset>

            </footer>
        
    </div>
    

<script type="text/javascript" src="/jira/s/d41d8cd98f00b204e9800998ecf8427e-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/1.0/_/download/batch/jira.webresources:bigpipe-js/jira.webresources:bigpipe-js.js" data-wrm-key="jira.webresources:bigpipe-js" data-wrm-batch-type="resource" data-initially-rendered></script>
<script type="text/javascript" src="/jira/s/d41d8cd98f00b204e9800998ecf8427e-CDN/-mou4xa/75005/b6b48b2829824b869586ac216d119363/1.0/_/download/batch/jira.webresources:bigpipe-init/jira.webresources:bigpipe-init.js" data-wrm-key="jira.webresources:bigpipe-init" data-wrm-batch-type="resource" data-initially-rendered></script>

<form id="jira_request_timing_info" class="dont-default-focus" >
	<fieldset class="parameters hidden">
		<input type="hidden" title="jira.request.start.millis" value="1507838306805" />
		<input type="hidden" title="jira.request.server.time" value="35" />
		<input type="hidden" title="jira.request.id" value="1018x445112x2" />
		<input type="hidden" title="jira.session.expiry.time" value="-" />
		<input type="hidden" title="jira.session.expiry.in.mins" value="-" />
		<input id="jiraConcurrentRequests" type="hidden" name="jira.request.concurrent.requests" value="2" />
		<input type="hidden" title="db.conns.time.in.ms" value="0" />
	</fieldset>
</form>
<!--
	                 REQUEST ID : 1018x445112x2
	          REQUEST TIMESTAMP : [12/Oct/2017:16:58:26 -0300]
	               REQUEST TIME : 0.0350
	                 ASESSIONID : -
	        CONCURRENT REQUESTS : 2

	                      db.conns : OpSnapshot{name='db.conns', invocationCount=1, elapsedTotal=203057, elapsedMin=203057, elapsedMax=203057, resultSetSize=0, cpuTotal=0, cpuMin=0, cpuMax=0}
-->

</body>
</html>
